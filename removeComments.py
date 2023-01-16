class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ret = []
        new_command = []
        inside_comment_block = False
        
        
        for command in source:
            if (not inside_comment_block):
                if (len(new_command)):
                    ret.append("".join(new_command))
                    
                new_command.clear()
                
            i = 0
            
            
            while (i < len(command)):
                i_next = i + 1
                
                
                if (not inside_comment_block and command[i] == "/"):
                    if (i_next < len(command)):
                        if (command[i_next] == "*"):
                            inside_comment_block = True
                            i = i_next
                        elif (command[i_next] == "/"):
                            break
                        else:
                            new_command.append("/")
                    else:
                        new_command.append("/")
                elif (command[i] == "*"):
                    if (inside_comment_block):
                        if (i_next < len(command) and command[i_next] == "/"):
                            inside_comment_block = False
                            i = i_next
                    else:
                        new_command.append("*")
                elif (not inside_comment_block):
                    new_command.append(command[i])
                else:
                    pass
                
                i += 1
        
        
        if (len(new_command)):
            ret.append("".join(new_command))
            
        return ret
