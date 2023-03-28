import string
import secrets

from app.internal.password.models.generate_password import GeneratePasswordModel


class GeneratePassword:
    switcher = {
        "low_case": string.ascii_lowercase,
        "upper_case": string.ascii_uppercase,
        "number": string.digits,
        "special_char": string.punctuation
    }

    def generate_password(self, specifications: GeneratePasswordModel) -> str:
        """
        Generate a random password based on the given specifications.

        Args:
            specifications: An instance of GeneratePasswordModel containing the desired specifications for the password.

        Returns:
            A string representing the generated password.
        """
        alphabet = self.__define_alphabet(specifications)
        password = ''.join(secrets.SystemRandom().choice(alphabet) for _ in range(specifications.length))
        return password

    def __define_alphabet(self, specifications: GeneratePasswordModel) -> str:
        """
        Define the alphabet to be used to generate the password based on the given specifications.

        Args:
            specifications: An instance of GeneratePasswordModel containing the desired specifications for the password.

        Returns:
            A string representing the alphabet to be used to generate the password.
        """
        alphabet = [self.switcher[switch] for switch in self.switcher.keys() if getattr(specifications, switch)]
        return ''.join(alphabet)
