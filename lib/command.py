class Command:
    command_stack = ['вперёд', 'назад', 'налево', 'направо']
    selected_command = None
    raw = {
        'alternative': [],
        'final': True
    }

    def __init__(self, speach_obj) -> None:
        self.raw = speach_obj
        print(speach_obj)

    def define_command(self):
        try:
            for i in range(len(self.command_stack)):
                for j in range(len(self.raw['alternative'])):
                    if(self.command_stack[i] in self.raw['alternative'][j]['transcript']):
                        self.selected_command = self.command_stack[i]
                        break

            return self
        except:
            return 'Command not find'

    def call_command(self):
        if(self.selected_command == 'вперёд'):
            print('Комманда вперед')
        elif(self.selected_command == 'назад'):
            print('Комманда назад')
        elif(self.selected_command == 'налево'):
            print('Комманда налево')
        elif(self.selected_command == 'направо'):   
            print('Комманда направо')
        else:
            print('Комманда не обнаружена')
        
        return self

    def print_command(self):
        print(self.selected_command)

        return self
    