
import time,os, subprocess, sys

# color output
class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[93m'
    OKRED = '\033[91m'
    ENDC = '\033[0m'

def log(message, type):
    switcher = {
        "info": bcolors.OKBLUE,
        "success": bcolors.OKGREEN,
        "warning": bcolors.OKYELLOW,
        "error": bcolors.OKRED,
    }
    print(switcher.get(type, "Invalid type") + "["+type.capitalize()+"] " + bcolors.ENDC + message)

def oscmd(command):
    # get output from command line
    os.system(command + " > logs.temp")
    # read output from file
    file = open("logs.temp", "r")
    output = file.read()
    file.close()
    # remove file
    os.remove("logs.temp")
    return output

def execute_cmd_in_terminal(command):
    os.system(f'start cmd /k "{command}"')
    #subprocess.Popen(["gnome-terminal", "--", "bash", "-c", command])

class Installation:

    def __init__(self):
        self.checkInstall()

    def checkInstall(self):
        self.checkNodeJS()
        self.checkNPM()
        self.checkCreateReactApp()
        self.checkAxios()
        self.checkReactRouter()

    def checkNodeJS(self):
    # Check if NodeJS is installed on the system depends on the OS Linux, Mac, Windows
        try:
            log("Checking NodeJS version...", "info")
            log(f"NodeJS version: {oscmd('node -v')}", "success")
        except:
            log("NodeJS is not installed", "error")
            log("Please install NodeJS : https://nodejs.org/en/download/", "warning")

    def checkNPM(self):
        try:
            log("Checking NPM version...", "info")
            log(f"NPM version: {oscmd('npm -v')}", "success")
        except:
            log("NPM is not installed", "error")
            log("Please install NPM : https://nodejs.org/en/download/", "error")
        
    # Verify if "create-react-app" is installed
    def checkCreateReactApp(self):
        try:
            log("Checking create-react-app version...", "info")
            log(f"create-react-app version: {oscmd('create-react-app -V')}", "success")
        except:
            log("create-react-app is not installed", "error")
            try:
                log("Installing create-react-app...", "info")
                os.system("npm install -g create-react-app")
                log("create-react-app installed successfully", "success")
            except:
                log("Error installing create-react-app", "error")
                log("Please try again", "error")

    def checkAxios(self):
        try:
            log("Checking axios version...", "info")
            log(f"axios version: {oscmd('npm axios -v')}", "success")
        except:
            log("axios is not installed", "error")
            try:
                log("Installing axios...", "info")
                os.system("npm install axios")
                log("axios installed successfully", "success")
            except:
                log("Error installing axios", "error")
                log("Please try again", "error")

    def checkReactRouter(self):
        try:
            log("Checking react-router-dom version...", "info")
            log(f"react-router-dom version: {oscmd('npm react-router-dom -v')}", "success")
        except:
            log("react-router-dom is not installed", "error")
            log("Please install react-router-dom", "error")
            try:
                log("Installing react-router-dom...", "info")
                os.system("npm install react-router-dom")
                log("react-router-dom installed successfully", "success")
            except:
                log("Error installing react-router-dom", "error")
                log("Please try again", "error")
                
def main():
    project_name = input("Enter project name: ").lower().replace(" ", "-")
    Installation().checkInstall()
    log("Creating react project...", "info")
    try:
        os.system(f"npx create-react-app {project_name}")
        log("React project created successfully", "success")
    except:
        log("Error creating react project", "error")
        log("Please try again", "error")
        exit()
    # Open terminal in project folder
    execute_cmd_in_terminal(f"cd {project_name} & npm start")
    sys.exit()

main()    