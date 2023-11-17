from flask import Flask, send_file, render_template
from pystyle import *
from threading import Thread

ascii = """
 ____                                   __      ______  ______     
/\  _`\                                /\ \    /\__  _\/\__  _\    
\ \,\L\_\  _____   _ __    __     __   \_\ \   \/_/\ \/\/_/\ \/    
 \/_\__ \ /\ '__`\/\`'__\/'__`\ /'__`\ /'_` \     \ \ \   \ \ \    
   /\ \L\ \ \ \L\ \ \ \//\  __//\  __//\ \L\ \     \_\ \__ \_\ \__ 
   \ `\____\ \ ,__/\ \_\\ \____\ \____\ \___,_\    /\_____\/\_____/
    \/_____/\ \ \/  \/_/ \/____/\/____/\/__,_ /    \/_____/\/_____/
             \ \_\                                                 
              \/_/     @Mxtsouko666              


"""         
ports="5000"

class Main():
    def main():
        def running():
                app = Flask('')

                @app.route('/')
                def main():
                    return send_file(f'{repository}')
                
                @app.route('/style')
                def css():
                    return send_file(f'{repository_css}')

                def run():
                    app.run(host="0.0.0.0", port=port_property)

                if __name__ == '__main__':
                    server = Thread(target=run)
                    server.start()

        print(Colorate.Diagonal(Colors.red_to_white,Center.XCenter(ascii)))
        repository = Write.Input("Please enter your repository file, index.html'>> ", Colors.red_to_white, interval=0.1)
        System.Clear()
        print(Colorate.Diagonal(Colors.red_to_white,Center.XCenter(ascii)))
        repository_css = Write.Input("Please enter your repository file, style.css'>> ", Colors.red_to_white, interval=0.1)
        System.Clear()
        print(Colorate.Diagonal(Colors.red_to_white,Center.XCenter(ascii)))
        port_property = Write.Input("Please enter your port or 5000'>> ", Colors.red_to_white, interval=0.1)
        if port_property == port_property or ports:
            running() 
 

if __name__ == '__main__':
    Main.main()

