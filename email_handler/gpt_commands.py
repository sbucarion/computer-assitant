list_of_commands = {
    "send_email_commands":[
                """Can you extract the, subject of the email, body of the email, attachment file name, email reciever, body of them email, and  the attachment file path from this text: """,
        
                """. And give the answer in the following format '{'"file_name": , "file_path": , "to": , "subject": , "body": '}' where 
                the file name is first, the file path for the file name is second, the email receiver as the third value, the subject as the fourth value, and the body as the fifth value. If the word subject or body is not in the text leave those parameters as empty strings
                and no other words in the response"""
    ]
    
}