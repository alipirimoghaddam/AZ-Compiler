import hashlib
import base64
import os
import sys
import az_theme as AZ

AZtheme = AZ.AZtheme

class AZCompiler:
    @staticmethod
    def derive_key(password: str, key_length: int = 32) -> bytes:
        """Derive a key from the password using SHA-256 hashing."""
        salt = b'az_salt_'  # Fixed salt for simplicity; in real use, generate random salt
        key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000, key_length)
        return key

    @staticmethod
    def xor_encrypt_decrypt(data: bytes, key: bytes) -> bytes:
        """Encrypt or decrypt data using XOR with the key."""
        return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

    @classmethod
    def compile_to_az(cls, source_file: str, password: str):
        """Compile a Python file to an encrypted .az file."""
        if not os.path.exists(source_file):
            AZtheme.error("File Error", f"Source file '{source_file}' not found.")
            return False

        with open(source_file, 'rb') as f:
            source_code = f.read()

        key = cls.derive_key(password)
        encrypted_code = cls.xor_encrypt_decrypt(source_code, key)
        encrypted_code_b64 = base64.b64encode(encrypted_code).decode('utf-8')

        az_file = source_file.replace('.py', '.az')
        with open(az_file, 'w') as f:
            f.write(encrypted_code_b64)

        AZtheme.success("Compilation", f"File compiled to {az_file}")
        return True

    @classmethod
    def run_az(cls, az_file: str, password: str):
        """Run an encrypted .az file by decrypting and executing it."""
        if not os.path.exists(az_file):
            AZtheme.error("File Error", f"File '{az_file}' not found.")
            return False

        with open(az_file, 'r') as f:
            encrypted_code_b64 = f.read()

        try:
            encrypted_code = base64.b64decode(encrypted_code_b64.encode('utf-8'))
        except Exception:
            AZtheme.error("Decryption Error", "Invalid .az file format.")
            return False

        key = cls.derive_key(password)
        decrypted_code = cls.xor_encrypt_decrypt(encrypted_code, key)

        try:
            exec(decrypted_code.decode('utf-8'))
        except Exception as e:
            AZtheme.error("Execution Error", str(e))
            return False

        return True


def interactive_mode():
    """Start an interactive mode for compiling and running files."""
    AZtheme.banner()
    AZtheme.info("Interactive Mode", "Type 'compile [file.py] [password]' or 'run [file.az] [password]'")
    AZtheme.info("Exit", "Type 'exit' to quit")

    while True:
        try:
            user_input = AZtheme.input("AZCompiler> ").strip()
            if not user_input:
                continue
            if user_input.lower() == 'exit':
                AZtheme.success("Exit", "Goodbye!")
                break

            parts = user_input.split()
            command = parts[0].lower()
            compiler = AZCompiler()

            if command == 'compile':
                if len(parts) < 3:
                    AZtheme.error("Syntax Error", "Usage: compile [file.py] [password]")
                else:
                    source_file = parts[1]
                    password = parts[2]
                    compiler.compile_to_az(source_file, password)
            elif command == 'run':
                if len(parts) < 3:
                    AZtheme.error("Syntax Error", "Usage: run [file.az] [password]")
                else:
                    az_file = parts[1]
                    password = parts[2]
                    compiler.run_az(az_file, password)
            else:
                AZtheme.error("Command Error", f"Unknown command '{command}'")
        except KeyboardInterrupt:
            AZtheme.error("Interrupted", "Exiting...")
            break
        except Exception as e:
            AZtheme.error("Unexpected Error", str(e))


def main():
    if len(sys.argv) == 1:
        interactive_mode()
    else:
        command = sys.argv[1]
        compiler = AZCompiler()

        if command == "compile":
            if len(sys.argv) < 4:
                AZtheme.error("Argument Error", "Missing file or password for compile.")
                sys.exit(1)
            source_file = sys.argv[2]
            password = sys.argv[3]
            compiler.compile_to_az(source_file, password)
        elif command == "run":
            if len(sys.argv) < 4:
                AZtheme.error("Argument Error", "Missing file or password for run.")
                sys.exit(1)
            az_file = sys.argv[2]
            password = sys.argv[3]
            compiler.run_az(az_file, password)
        else:
            AZtheme.error("Command Error", f"Unknown command '{command}'")


if __name__ == "__main__":
    main()