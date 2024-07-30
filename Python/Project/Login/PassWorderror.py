#密码错误异常
class PasswordError(Exception):
    def __init__(self, message = "Password is incorrent") -> None:
        self.message = message
        super().__init__(self.message)