class RuntimeErrorWithCode(TypeError):
    """
    Exceptin raised with a specific error code is needed.
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code


err = RuntimeErrorWithCode('Ouch!! Error.', 500)
print(err)
