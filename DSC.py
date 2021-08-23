import sys, time, os

class Main:
    def __init__(self):
        self.commands_list = ['help', 'list-ou-devices', 'list-in-devices', 'set-default-output', 'set-default-input', 'exit']
    
    def list_out_devices(self):
        
        os.system('pactl list short sinks')
        print('\n \033[32m **Please, copy the text that is between the first number and the word "module" with Ctrl + Shift + C to select the output device\033[m')
    
    def list_in_devices(self):
        os.system('pactl list short sources')
        print('\n \033[32m **Please, copy the text that is between the first number and the word "module" with Ctrl + Shift + C to select the input device\033[m')
    
    def set_default_output(self, target_device):
        self.loading_bar()
        print('\n')
        os.system('pacmd set-default-sink '+target_device)
    
    def set_default_input(self, target_device):
        self.loading_bar()
        print('\n')
        os.system('pacmd set-default-source '+target_device)
    
    def exit(self):
        os.system('exit')
            
    def interface(self):
        while True:
            try:
                
                command = input('DSC >>> ')
            except:
                print('Error: unknown command')
                continue
            else:
                if command not in self.commands_list:
                    print('Error: Unknown command, type help to see the commands')
        
                
                elif command == self.commands_list[0]:
                   
                    '╔╠╚═'
                    print('╔════════════════════════')
                    for c in self.commands_list:
                        print('╠ '+c)
                    print('╚════════════════════════')
                
                elif command == self.commands_list[1]:
                    self.list_out_devices()

                elif command == self.commands_list[2]:
                    self.list_in_devices()

                elif command == self.commands_list[3]:
                    print('if you dont know which device, press enter and type list-ou-devices')
                    device = input('which device? >>> ')
                    self.set_default_output(device)
                
                elif command == self.commands_list[4]:
                    print('if you dont know which device, press enter and type list-ou-devices')
                    device = input('which device? >>> ')
                    self.set_default_input(device)
                elif command == 'exit':
                    break
    def loading_bar(self):
        sys.stdout.write('\033[32mConfiguring...\033[m\n')
        bar_width = 40
        sys.stdout.write('[{}]'.format(' '*bar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (bar_width+1))
        for i in range(bar_width):
            sys.stdout.write('▉')
            
            sys.stdout.flush()
            time.sleep(0.05)
        sys.stdout.write(']')

def menu_fodastico(width, height, message):
    print('┎',end='')
    for r in range(width):
        print('━',end='')
    print('┒')

    for c in range(height):
        print('┃' + (' '*width) + '┃')
        if c == height -1:
            print('┃' + ('≛ '+message+' ≛').center(width) + '┃')
    
    print('┖',end='')
    for r in range(width):
        print('━',end='')
    print('┚')

menu_fodastico(50, 3, 'Welcome to Default Sound Configurator')

print('type help to see the commands')
if __name__ == "__main__":
    Main().interface()