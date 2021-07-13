import mind_map.IO as mind_IO
import mind_map.process as mind_process
import mind_map.draw as mind_draw
import mind_map.kg as mind_kg
from shutil import copyfile
import web_show

if __name__ == '__main__':
    # Method 1: Load Xmind file(certain file)
    #data = mind_IO.load_dataset("./test.xmind")

    # Method 2: Load Xmind file(multipul files)
    mind_process.set_base_path("../KnowledgeMap")#"./resources"
    data = mind_process.load_dataset("./计算机科学/计算机网络/计算机网络.xmind")
    
    # Print Data
    #mind_process.print_json(data)

    # Drawing preprocess
    data = mind_process.draw_init(data)
    
    # Change json to neoj4 type
    #mind_kg.change_to_pair(data)

    # Make defined type Node to show
    #data = mind_process.data_filter(data,kind="Structure")

    # Draw into html (by echarts)
    html_name = 'render.html'
    mind_draw.draw_html(data,name=html_name,temp=False)

    # Put html into xwpython to show
    # This step is to copy the html file to local server,
    # and open it by net. You can also just open render.html
    # to check.
    source = html_name
    target = "/usr/local/var/www/index.html"
    copyfile(source, target)
    web_show.run()

