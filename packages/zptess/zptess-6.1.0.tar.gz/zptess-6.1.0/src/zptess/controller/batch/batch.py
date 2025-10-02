# ----------------------------------------------------------------------
# Copyright (c) 2024 Rafael Gonzalez.
#
# See the LICENSE file for details
# ----------------------------------------------------------------------

# --------------------
# System wide imports
# -------------------

import os
import logging
import zipfile

from datetime import datetime, timezone
from typing import Tuple, Iterable

# ---------------------------
# Third-party library imports
# ----------------------------

from sqlalchemy import select, delete, func

from zptessdao.asyncio import Batch, SummaryView

# --------------
# local imports
# -------------

from ...dao import Session

# -----------------------
# Module global variables
# -----------------------

# get the module logger
log = logging.getLogger(__name__.split(".")[-1])


# ------------------
# Auxiliar functions
# ------------------


def get_paths(directory: str) -> Iterable:
    """Get all file paths in a list"""
    file_paths = list()
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        root = os.path.basename(root)  # Needs a change of cwd later on if we do this
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


def pack(base_dir: str, zip_file: str):
    """Pack all files in the ZIP file given by options"""
    paths = get_paths(base_dir)
    log.info(f"Creating ZIP File: '{os.path.basename(zip_file)}'")
    with zipfile.ZipFile(zip_file, "w") as myzip:
        for myfile in paths:
            myzip.write(myfile)


class Controller:
    def __init__(self):
        self.Session = Session

    async def open(self, comment: str | None) -> datetime:
        begin_tstamp = datetime.now(timezone.utc).replace(microsecond=0)
        async with self.Session() as session:
            async with session.begin():
                await self._assert_closed(session)
                batch = Batch(
                    begin_tstamp=begin_tstamp, end_tstamp=None, email_sent=False, comment=comment
                )
                session.add(batch)
        return begin_tstamp

    async def is_open(self) -> bool:
        async with self.Session() as session:
            return await self._is_open(session)

    async def get_open(self) -> Batch:
        """Used by the persistent controller"""
        async with self.Session() as session:
            return await self._get_open(session)

    async def latest(self, load_summaries: bool = False) -> Batch | None:
        """Used by the persistent controller"""
        async with self.Session() as session:
            return await self._latest(session, load_summaries)

    async def by_date(self, tstamp: datetime, load_summaries: bool = False) -> Batch | None:
        async with self.Session() as session:
            return await self._by_date(session, tstamp)

    async def close(self) -> Tuple[datetime, datetime, int]:
        end_tstamp = datetime.now(timezone.utc).replace(microsecond=0)
        async with self.Session() as session:
            async with session.begin():
                await self._assert_open(session)
                batch = await self._get_open(session)
                t0 = batch.begin_tstamp
                t1 = end_tstamp
                # We count summaries even if the upd_flag is False
                q = (
                    select(func.count("*"))
                    .select_from(SummaryView)
                    .where(SummaryView.session.between(t0, t1))
                )
                N = (await session.scalars(q)).one()
                batch.end_tstamp = end_tstamp
                batch.email_sent = False
                batch.calibrations = N
                session.add(batch)
        return t0, t1, N

    async def purge(self) -> int:
        async with self.Session() as session:
            async with session.begin():
                stmt = delete(Batch).where(Batch.calibrations == 0, Batch.end_tstamp.is_not(None))
                result = await session.execute(stmt)
                return result.rowcount

    async def orphan(self) -> set:
        in_batches = set()
        all_summaries = set()
        async with self.Session() as session:
            async with session.begin():
                q = select(Batch.begin_tstamp, Batch.end_tstamp).where(
                    Batch.end_tstamp.is_not(None)
                )
                batches = (await session.execute(q)).all()
                q = select(SummaryView.session)
                all_summaries = set((await session.scalars(q)).all())
                for t0, t1 in batches:
                    q = select(SummaryView.session).where(SummaryView.session.between(t0, t1))
                    summaries = (await session.scalars(q)).all()
                    in_batches.update(set(summaries))
        return all_summaries - in_batches

    async def view(
        self,
    ) -> Iterable[Tuple[datetime, datetime, bool, int, str]]:
        async with self.Session() as session:
            async with session.begin():
                q = select(
                    Batch.begin_tstamp,
                    Batch.end_tstamp,
                    Batch.calibrations,
                    Batch.email_sent,
                    Batch.comment,
                ).order_by(Batch.begin_tstamp.desc())
                batches = (await session.execute(q)).all()
        return batches

    async def export(self, path: str) -> None:
        pass

    # ----------------
    # Helper functions
    # ----------------

    async def _is_open(
        self,
        session: Session,
    ) -> bool:
        q = select(func.count("*")).select_from(Batch).where(Batch.end_tstamp.is_(None))
        count = (await session.scalars(q)).one()
        return count > 0

    async def _get_open(
        self,
        session: Session,
    ) -> Batch | None:
        q = select(Batch).where(Batch.end_tstamp.is_(None))
        batch = (await session.scalars(q)).one_or_none()
        return batch

    async def _latest(
        self,
        session: Session,
        load_summaries: bool,
    ) -> Batch | None:
        sub_q = select(func.max(Batch.begin_tstamp))
        q = select(Batch).where(Batch.begin_tstamp.in_(sub_q))
        batch = (await session.scalars(q)).one()
        if load_summaries:
            summaries = await batch.awaitable_attrs.summaries
            for summary in summaries:
                await summary.awaitable_attrs.photometer
        return batch

    async def _by_date(
        self,
        session: Session,
        tstamp: datetime,
        load_summaries: bool,
    ) -> Batch | None:
        q = select(Batch).where(Batch.begin_tstamp == tstamp)
        batch = (await session.scalars(q)).one_or_none()
        if batch and load_summaries:
            summaries = await batch.awaitable_attrs.summaries
            for summary in summaries:
                await summary.awaitable_attrs.photometer
        return batch

    async def _assert_closed(
        self,
        session: Session,
    ) -> None:
        already_open = await self._is_open(session)
        if already_open:
            raise RuntimeError("Batch already open!")

    async def _assert_open(
        self,
        session: Session,
    ) -> None:
        already_open = await self._is_open(session)
        if not already_open:
            raise RuntimeError("Batch already closed!")
