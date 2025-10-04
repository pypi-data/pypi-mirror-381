import time,os,inspect,json

@staticmethod
def msg(
    msg = None,
    handle = 'info',
    sleep = 0
):
    """""""""""""""""""""""""""""""""
    
    
    
    
    
    
    
    
    
    
    
    """""""""""""""""""""""""""""""""

    
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
    if fnName == '<module>': 
        fnName = ''
    else: 
        fnName = f' def {fnName}()'
    print(f"{emoji}{handleTextColor}TensorPyOps: {colors['text']['GREEN']}{namespace}{colors['text']['MAGENTA']}{fnName} LINE {callerFrame.lineno} {msg}")