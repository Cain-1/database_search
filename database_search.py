import colorama
import os,sys
def main():
    print(colorama.Style.NORMAL + colorama.Fore.RED + "")
    folder_path = input("database path: ")
    search = input("search in database: ")
    with open(os.path.join(folder_path),'r',encoding="utf-8",errors='ignore')as file:
        for line in file:
            if search in line:
                print(f"{line.strip()}")

        back = input("back? 1/2")
        match back:
            case "1":
                main()
            case _:
                sys.exit()
main()  
