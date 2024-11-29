# Open txt file to read informations
with open(".\\user_information.txt", "r") as profile_identifier:
    # Ask user for a full name
    while True:
        name = input('Input a full name to identify information: ')
        
        
        # Read the informations in txt file
        user_information = profile_identifier.read()
        lines = user_information.split('\n\n')
        
        

        # Use for loop to identify the name in txt file
        for line in lines:
         if name in line:
            print('Identified', line.strip())
            break
   
        if name not in line:
           print('No information can be found')
        
        another_entry = input('Do you want to find another user?: ')
        if another_entry != 'yes':
           break
               
            
        
            
            
                     
       
         
      
     
                
