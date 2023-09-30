import logging

def count_files(file_name): 
    
    file = None
    
    try: 
        
        file = open(file_name,'r')
        lines = file.readlines()

    except TypeError as e: 
        logging.error(e)
        return 0
        
    except EnvironmentError as e: 
        logging.error(e.args)
    except UnicodeDecodeError as e: 
        logging.error(e)
        return 0
    else: 
        return len(lines)
    finally: 
        if file: 
            print(len(lines))
            file.close()
        
        
        
count_files('data.csv')
        