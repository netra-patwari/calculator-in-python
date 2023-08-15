import re
from datetime import datetime

if __name__ =='__main__' :
    
    def calc():
        pattern = r'^[0-9+\-*()\/.\s]+$'
        
        def logs(time_statement):
            base = 'calcdatabase.txt'
            with open(base, 'a') as f:
                f.write(time_statement)

        while True:
            num_opr = input("Calculator mode activated (press 'q' to quit): ")
            current_time = datetime.now()
            timestamp = current_time.strftime('%d %b %Y - %H:%M:%S')
            
            time_quit = f'{timestamp} : calc quit\n\n'

            if num_opr.lower() == 'q':
                logs(time_quit)
                break
            
            if not re.match(pattern, num_opr):
                error = "Invalid input."
                print(error)
                time_error = f'\n{timestamp} : {error}'
                logs(time_error)
                
            try:
                result = eval(num_opr)
                print(f"{num_opr} = ", result)
                s = f'\n{timestamp} : {num_opr} = {result}'
                logs(s)

            except Exception as e:
                print("Error:", e)

    calc()
