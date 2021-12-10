import os
import subprocess

def pdf_table(df, out_path=None):
    """Create a markdown/pdf table from a Pandas DataFrame

    Args:
        df ([type]): [description]
        out_path ([type]): [description]    
    
    Examples:
        import pandas as pd
        df = pd.DataFrame(zip(["a"], ["d"]), columns = ["b", "c"])
        out_path = "test.pdf"
    """
    if out_path is None:
        return df.to_markdown()
    
    df.to_markdown("test.md")

    f = open('test.md','r')
    newf = open('test_gobble.md','w')
    lines = f.readlines() # read old content
    newf.write("\pagenumbering{gobble}\n")
    for line in lines: # write old content after new
        newf.write(line)
    newf.close()
    f.close()

    subprocess.call("pandoc -s test_gobble.md -o " + out_path, shell=True)
    try:
        subprocess.call("pdfcrop " + out_path + " " + out_path)
    except:
        pass
    os.remove("test.md")
    os.remove("test_gobble.md")    
    
    return out_path
