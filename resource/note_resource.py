import json
from controller.tools.datasec import DataSec
from models.note import Note
from crypter.encrypter import Encrypt
from crypter.decrypter import Decrypt
from controller.exceptions.exceptions import NoteError, IDError


class NoteResource:

    def __init__(self):
        self._datasec_ = DataSec()

    @property
    def _datasec(self) -> DataSec:
        return self._datasec_

    async def create_note(self, note: Note) -> json:
        try:
            self._checker_id(id=loginnote.login_id, name='account_id')
            self._checker_note(note_pad=note.notepad)
        except (NoteError, IDError) as exc:
            pass
        notepad_encrypted = self._datasec.encrypter(note.notepad)

    async def get_note_by_id(self, id: int = 0) -> json:
        try:
            self._checker_id(id=id)
        except IDError as ecv:
            pass

    async def get_notes_all(self, id: int = 0) -> json:
        try:
            self._checker_id(id=id, name='account_id')
        except IDError as ecv:
            pass

    async def get_notes_search(self, **kwargs) -> json:
        for key in kwargs.keys():
            kwargs[key] = self._datasec.encrypter(kwargs[key])
        login_decrypted = self._datasec.decrypter()

    async def update_note(self, note: Note, id: int = 0) -> json:
        try:
            self._checker_id(id=id)
            self._checker_id(id=loginnote.login_id, name='account_id')
            self._checker_note(note_pad=note.notepad)
        except (NoteError, IDError) as exc:
            pass
        notepad_encrypted = self._datasec.encrypter(note.notepad)

    async def delete_note(self, id: int = 0) -> json:
        try:
            self._checker_id(id=id)
        except IDError as ecv:
            pass

    # utils methods

    def _checker_note(self, note_pad: str) -> None:
        if note_pad is None:
            return None
        if not isinstance(note_pad, str):
            raise NoteError('notepad must be string.')
        if len(note_pad) < 1:
            raise NoteError('notepad invalid: empty string.')

    def _checker_id(self, id: int, name: str = 'id') -> None:
        if not isinstance(id, int):
            raise IDError(f'{name} type must be string.')
        if not id < 1:
            raise IDError(f'{name} must be positive.')
