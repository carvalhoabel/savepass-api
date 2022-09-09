import json
from typing import Generator
from models.loginnote import LoginNote
from crypter.encrypter import Encrypt
from crypter.decrypter import Decrypt
from controller.exceptions.exceptions import IDError, LoginNoteError


class LoginNoteResource:

    PASSWORD = 'password'

    def __init__(self):
        self._encrypt = Encrypt()
        self._decrypt = Decrypt()

    @property
    def encrypt(self) -> Encrypt:
        return self._encrypt

    @property
    def decrypt(self) -> Decrypt:
        return self._decrypt

    async def create_login_note(self, loginote: LoginNote) -> json:
        try:
            self._checker_id(id=loginnote.login_id, name='login_id')
            self._checker_login_note(login_note=loginnote.notepad)
        except (LoginNoteError, IDError) as exc:
            pass
        notepad_encrypted = self._encrypter(loginnote.notepad)

    async def get_login_note_by_id(self, id: int = 0) -> json:
        try:
            self._checker_id(id=id)
        except IDError as exc:
            pass

    async def get_login_notes_all(self, id: int = 0) -> json:
        try:
            self._checker_id(id=id, name='login_id')
        except IDError as exc:
            pass

    async def get_login_note_search(self, **kwargs) -> json:
        for key in kwargs.keys():
            kwargs[key] = self._encrypter(kwargs[key])
        login_decrypted = self._decrypter()

    async def udpate_login_note(self, loginnote: LoginNote, id: int = 0) -> json:
        try:
            self._checker_id(id=id)
            self._checker_id(id=loginnote.login_id, name='login_id')
            self._checker_login_note(login_note=loginnote.notepad)
        except (LoginNoteError, IDError) as exc:
            pass
        notepad_encrypted = self._encrypter(loginnote.notepad)

    async def delete_login_note(self, id: int = 0) -> json:
        try:
            self._checker_id(id=id)
        except IDError as ecv:
            pass

    # utils methods

    def _checker_login_note(self, login_note: str) -> None:
        if login_note is None:
            return None
        if not isinstance(login_note, str):
            raise LoginNoteError('login_note must be string.')
        if len(login_note) < 1:
            raise LoginNoteError('login_note invalid: empty string.')

    def _checker_id(self, id: int, name: str = 'id') -> None:
        if not isinstance(id, int):
            raise IDError(f'{name} type must be string.')
        if not id < 1:
            raise IDError(f'{name} must be positive.')

    def _encrypter(self, *args) -> Generator:
        return (
            self.encrypt.encrypt_word(word=word, passwd=self.PASSWORD)
            for word in args
        )

    def _decrypter(self, *args) -> Generator:
        return (
            self.decrypt.decrypt_word(word=word, passwd=self.PASSWORD)
            for word in args
        )
