import datetime

print("Welcome to the Personal Data Manager!")
class JournalManager:

    def __init__(self):
        self.__filename = "journal.txt"

        try:
            file = open(self.__filename, "r")
            file.close()

        except FileNotFoundError:
            try:
                file = open(self.__filename, "x")
                file.close()

            except OSError as e:
                print("File error:", e)

        except OSError as e:
            print("File error:", e)

    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry:\n")

            if not entry.strip():
                print("\nJournal entry cannot be empty!")
                return

            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            file = open(self.__filename, "a")

            try:
                file.write(f"[{time}]\n")
                file.write("-" * 35 + "\n")
                file.write(entry + "\n\n")

                print("\nYour entry has been successfully added!")

            finally:
                file.close()

        except PermissionError:
            print("\nPermission denied! You cannot write to this file.")

        except OSError as e:
            print("\nFile error:", e)

    def view_entry(self):
        try:
            file = open(self.__filename, "r")

            try:
                entries = file.read()

                if not entries.strip():
                    print("\nYour journal is empty.")

                else:
                    print("\nYour Journal Entries:")
                    print("=" * 30)
                    print(entries)

            finally:
                file.close()

        except FileNotFoundError:
            print("\nNo journal file found. Add a new entry first.")

        except PermissionError:
            print("\nPermission denied! You cannot read this file.")

        except OSError as e:
            print("\nFile error:", e)

    def search_entry(self):
        try:
            keyword = input("\nEnter a keyword or date to search: ").strip()

            if keyword == "":
                raise ValueError("Search keyword cannot be empty.")

            file = open(self.__filename, "r")

            try:
                entries = file.read()

            finally:
                file.close()

            if not entries.strip():
                print("\nYour journal is empty.")
                return

            all_entries = entries.split("\n\n")
            found = False

            for entry in all_entries:
                if keyword.lower() in entry.lower():

                    if not found:
                        print("\nMatching Entries:")
                        print("-" * 35)

                    print(entry.strip())
                    found = True

            if not found:
                print(f"\nNo entries were found for: {keyword}.")

        except FileNotFoundError:
            print("\nJournal file does not exist.")

        except ValueError as e:
            print("\nInvalid input:", e)

        except PermissionError:
            print("\nPermission denied! You cannot read this file.")

        except OSError as e:
            print("\nFile error:", e)

    def delete_entries(self):
        try:
            file = open(self.__filename, "r")
            file.close()

            confirm = input("\nAre you sure you want to delete all entries? (yes/no):").strip().lower()

            if confirm == "yes":
                file = open(self.__filename, "w")

                try:
                    file.write("")

                finally:
                    file.close()

                print("\nAll journal entries have been deleted.")

            elif confirm == "no":
                print("\nDeletion cancelled.")

            else:
                raise ValueError("Please enter yes or no.")

        except FileNotFoundError:
            print("\nJournal file does not exist.")

        except ValueError as e:
            print("\nInvalid input:", e)

        except PermissionError:
            print("\nPermission denied! You cannot modify this file.")

        except OSError as e:
            print("\nFile error:", e)

    def menu(self):
        while True:
            try:
                print("\nPlease select an option:")
                print("1. Add New Entry")
                print("2. View All Entries")
                print("3. Search for an Entry")
                print("4. Delete All Entries")
                print("5. Exit")

                choice = int(input("\nEnter your choice: "))

                if choice == 1:
                    self.add_entry()

                elif choice == 2:
                    self.view_entry()

                elif choice == 3:
                    self.search_entry()

                elif choice == 4:
                    self.delete_entries()

                elif choice == 5:
                    print("\nThank you for using Personal Data Manager!")
                    break

                else:
                    raise ValueError("Please select a valid option from 1 to 5.")

            except ValueError as e:
                print("\nInvalid input:", e)


my_journal = JournalManager()
my_journal.menu()

