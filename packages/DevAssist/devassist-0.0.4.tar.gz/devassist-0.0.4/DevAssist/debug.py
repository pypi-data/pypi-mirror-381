import time,os,inspect,json,traceback
from tabulate import tabulate

@staticmethod
def msg(
    msg = None,
    handle = 'info',
    sleep = 0
):
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    callerFrame = inspect.stack()[1]
    
    callerPath = os.path.abspath(callerFrame.filename)
    
    rootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    colors = {
        'text': {
            
            'BLACK': '\033[30m',
            'RED': '\033[31m',
            'GREEN': '\033[32m',
            'YELLOW': '\033[33m',
            'BLUE': '\033[34m',
            'MAGENTA': '\033[35m',  
            'CYAN': '\033[36m',
            'WHITE': '\033[37m',
            
            
            'BRIGHT_BLACK': '\033[90m',
            'BRIGHT_RED': '\033[91m',
            'BRIGHT_GREEN': '\033[92m',
            'BRIGHT_YELLOW': '\033[93m',
            'BRIGHT_BLUE': '\033[94m',
            'BRIGHT_MAGENTA': '\033[95m',
            'BRIGHT_CYAN': '\033[96m',
            'BRIGHT_WHITE': '\033[97m',
            
            'RESET': '\033[0m'  
        },
        'bg': {
            
            'BLACK': '\033[40m',
            'RED': '\033[41m',
            'GREEN': '\033[42m',
            'YELLOW': '\033[43m',
            'BLUE': '\033[44m',
            'MAGENTA': '\033[45m',
            'CYAN': '\033[46m',
            'WHITE': '\033[47m',
            
            
            'BRIGHT_BLACK': '\033[100m',
            'BRIGHT_RED': '\033[101m',
            'BRIGHT_GREEN': '\033[102m',
            'BRIGHT_YELLOW': '\033[103m',
            'BRIGHT_BLUE': '\033[104m',
            'BRIGHT_MAGENTA': '\033[105m',
            'BRIGHT_CYAN': '\033[106m',
            'BRIGHT_WHITE': '\033[107m',
            
            'RESET': '\033[0m'  
        }
    }
    
    time.sleep(sleep)

    if sleep > 0:
        msg = f"{msg} Pause for {sleep} seconds to continue executing the script"
    if isinstance(msg,dict) or isinstance(msg,list):
        try:
            msg = json.dumps(msg,ensure_ascii=False,indent=4)
        except:
            pass
    emoji = '🐞'
    handleTextColor = colors['text']['RED']
    if handle == 'error':
        emoji = '🐞'
        msg = f"{colors['text']['RED']}{msg}{colors['text']['RESET']}"
    elif handle == 'warning':
        emoji = '🍤'
        msg = f"{colors['text']['MAGENTA']}{msg}{colors['text']['RESET']}"
    elif handle == 'info':
        emoji = '🚩'
        msg = f"{colors['text']['CYAN']}{msg}{colors['text']['RESET']}"
    elif handle == 'success':
        emoji = '🌴'
        handleTextColor = colors['text']['RED']
        msg = f"{colors['text']['GREEN']}{msg}{colors['text']['RESET']}"
    else:
        msg = f"{colors['text']['RED']}{msg}{colors['text']['RESET']}"
    
    
    callerPath = callerPath.replace('.py', '')
    
    namespace = '.'.join(part.capitalize() for part in os.path.relpath(callerPath,rootDir).split('/'))

    fnName = callerFrame.function
    if fnName == '<module>' or handle == 'error': 
        fnName = ''
    else: 
        fnName = f' def {fnName}()'

    line = f'LINE {callerFrame.lineno}'
    if handle == 'error': 
        line = ''
    print(f"{emoji}{handleTextColor}TensorPyOps: {colors['text']['GREEN']}{namespace}{colors['text']['MAGENTA']}{fnName} {line} {msg}")

def error(
    message = '',
    handle = 'value'
):
    
    
    
    
    
    
    try:
        if handle == 'syntax':
            
            raise SyntaxError(message)
        elif handle == 'type':
            
            raise TypeError(message)
        elif handle == 'value':
            
            raise ValueError(message)
        elif handle == 'index':
            
            raise IndexError(message)
        elif handle == 'key':
            
            raise KeyError(message)
        elif handle == 'file':
            
            raise FileNotFoundError(message)
        elif handle == 'io':
            
            raise IOError(message)
        elif handle == 'os':
            
            raise OSError(message)
        elif handle == 'module':
            
            raise ModuleNotFoundError(message)
        elif handle == 'attribute':
            
            raise AttributeError(message)
        elif handle == 'name':
            
            raise NameError(message)
        elif handle == 'permission':
            
            raise PermissionError(message)
        else:
            msg(msg = 'Unknown error', handle = 'error')
    except Exception as e:
        msg(msg = f'{type(e).__name__}: {e}', handle = 'error')
def trace(e):
    
    
    
    
    
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

    
    BOLD = '\033[1m'

    tb = traceback.extract_tb(e.__traceback__)
    table_data = []
    for frame in tb:
        table_data.append([f'{CYAN}{frame.filename}{RESET}', f'{GREEN}{frame.lineno}{RESET}', f'{YELLOW}{frame.name}{RESET}', f'{RED}{frame.line}{RESET}'])
    
    table = tabulate(table_data, headers=[f'{BOLD}Error file name{RESET}', f'{BOLD}Line number{RESET}', f'{BOLD}Function name{RESET}', f'{BOLD}Line of code{RESET}'], tablefmt="grid")
    print('\n')
    print(f'{BOLD}⛵️ {RED}{e}{RESET}')
    print(table)
    print('\n')