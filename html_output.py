class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    def output_html(self):
        fout=open('output','a+')
        for data in self.datas:
            for da in data:
                fout.write(str(da)+'\n')
        fout.close()