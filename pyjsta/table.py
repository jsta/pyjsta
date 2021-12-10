import os
import subprocess
import plotly.graph_objects as go


def plotly_table(df, col_format=[], pdf_path=None, hgt=None, wth=None):
    """> View or print a pandas DataFrame as a plotly table 

    Args:
        df ([type]): [description]
        pdf_path ([type], optional): [description]. Defaults to None.

    Returns:
        [type]: [description]

    Examples:
    ```python
    import pandas as pd
    # hgt = 400
    # wth = hgt * 1.55
    df = pd.DataFrame(zip(["0.01544"], ["d"]), columns = ["b", "c"])    
    pyjsta.plotly_table(df, col_format = [".2f", ""])    
    ```
    """
    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=list(df.columns),
                    fill_color='paleturquoise',
                    align='left'
                ),
                cells=dict(
                    values=[df[col] for col in df.columns],
                    fill_color='lavender',
                    align='left',
                    format=col_format
                )
            )
        ]
    )
    if pdf_path is None:
        return fig.show()

    fig.write_image("myimage.png", height=hgt, width=wth)

    return None


def md_table(df, pdf_path=None):
    """> View or print a pandas DataFrame as a markdown table     

    Args:
        df ([type]): [description]
        pdf_path ([type]): [description]    
    
    Examples:
    ```python
    import pandas as pd
    df = pd.DataFrame(zip(["a"], ["d"]), columns = ["b", "c"])
    pyjsta.md_table(df, "test.pdf")
    ```
    """
    if pdf_path is None:
        return df.to_markdown()

    df.to_markdown("test.md")

    f = open('test.md', 'r')
    newf = open('test_gobble.md', 'w')
    lines = f.readlines() # read old content
    newf.write("\pagenumbering{gobble}\n")
    for line in lines:    # write old content after new
        newf.write(line)
    newf.close()
    f.close()

    subprocess.call("pandoc -s test_gobble.md -o " + pdf_path, shell=True)
    try:
        subprocess.call("pdfcrop " + pdf_path + " " + pdf_path)
    except:
        pass
    os.remove("test.md")
    os.remove("test_gobble.md")

    return pdf_path
