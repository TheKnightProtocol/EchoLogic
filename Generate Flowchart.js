# flowchart_generator.py                                                                                                                               
def                                generate_mermaid_flowchart(actions):
    chart = "graph TD\n"    
    for i, step in        enumerate(actions):      
        chart += f"    Step{i}[{step}]\n"
        if i > 0: 
            chart += f"    Step{i-1} --> Step{i}\n"     
    return chart          
                        
    
  
