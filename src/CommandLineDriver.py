class CLI:
    log = logging.getLogger()
    def run(self):
        self.header()
        log.debug("Running in DEBUG mode")

    def header(self):
        title = """   _____      __  __    ___              __      ____     __            
  / __(____ _/ / / /_  / _ \__ ________ / ___   / _____  / _  _____ ____
 / _// / _ `/ _ / __/ / ___/ // /_ /_ // / -_) _\ \/ _ \/ | |/ / -_/ __/
/___/_/\_, /_//_\__/ /_/   \_,_//__/__/_/\__/ /___/\___/_/|___/\__/_/   
------/___/-----------------------------------------------------------
BY SHAWN LONG
        """
        print(title)

if __name__ == '__main__':
    cli = CLI()
    cli.run()