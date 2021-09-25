ATGCU_dict={'A': 'T', 'a': 't', 'T': 'A', 't':'a', 'C': 'G', 'c':'g', 'G':'C', 'g':'c', 'U':'A', 'u':'a'}
alphabet = ['A', 'a', 'T', 't', 'G', 'g', 'C', 'c', 'U', 'u']
valid_commands = ['transcribe', 'reverse', 'complement', 'reverse complement', 'exit']


def valid_seq(seq):
    if not set([*seq.upper()]).issubset(set(['A', 'C', 'G', 'T', 'U'])):
        print('Wrong letters')
        return False
           
    if 'T' in seq.upper() and 'U' in seq.upper():
        print('T and U in the same sequence ')
        return False
           
    return True
           
def get_valid_seq():
    seq = input('Enter sequence ')
    while not valid_seq(seq):
        seq = input('Enter sequence ')
    return seq


def valid_command(command):
    if not command in valid_commands:
        print('Wrong command')
        return False
    return True

def get_valid_command():
    command = input('Enter command ')
    while not valid_command(command):
        command = input('Enter command ')
    return command
    
    
        
    
    
while True:
    
    command = get_valid_command()
    
    if command == 'exit':
        print('Bye')
        break

    seq = get_valid_seq()


    if command == 'transcribe':
        transcribe_seq = ''
        for i in range(len(seq)):
            if seq[i] == 'T':
                transcribe_seq += 'U'
            elif seq[i] == 't':
                transcribe_seq += 'u'
            else: 
                transcribe_seq  += seq[i]
        print(transcribe_seq)

            
    elif command == 'reverse':
        print(seq[::-1])
    
        
    elif command == 'complement':
        complement_seq = ''
        for i in range(len(seq)):
            complement_seq += ATGCU_dict[seq[i]]
        print (complement_seq)
            

    elif command == 'reverse complement':
        complement_seq = ''
        for i in range(len(seq)):
            complement_seq += ATGCU_dict[seq[i]]
        print (complement_seq[::-1])


        