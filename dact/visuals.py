def ascii_dact():
    print('\033[36m' + """
                                                                                                 
                                                                 `+:.                               
                                                                 .:oso/.                            
                                                                    `:+so/-                         
                  s.                                             +oo+-``:+ss/-`                     
                  s.                            `/               oso+ss+:``-/ss+-`                  
          -//////:s.   .:::::/:.      -:/::::-  .s:::-           oso  -/os+:. -/os+:                
        .o:`     `s.          `o-   .o:`        .s               oso     ./oso:` .:.    `-:         
        o:        s.      ```` //   o:          .s               oso        .:/     .:/osso-        
        o-        s.   :/::--::o/   s-          .s               oso           `-/+sss+:-`          
        /+        s.  :+       //   +/          .s               oso       .:/osso/:.  .:/          
        `/+-`   `.s.  .o-`   `-o/   `/+-`    `  `o-              oso  `-:+sss+:-` `-/osso/.         
          `-:::::-.    `-::::-``-     `-:::::-   `-::-           oso/osso/:.  .:+oso+:.             
                                                                 oss+/-` `-/+sso/-`                 
                                                                     .:/oss+:.`                     
                                                                 .:+sso/-.                          
                                                                 .+:-`                              
                                                                                                    
                                                                                         
    
    
     """ + '\033[0m')



def complete_msg(app_name):
    ascii_dact()

    print("Setup Complete! ")
    print("""
        To Start the server write the following commands: 
            1. cd %s
            2. python manage.py runserver (Windows)
               python3 manage.py runserver (Others)

        HAPPY HACKING!! 
     """%(app_name))
