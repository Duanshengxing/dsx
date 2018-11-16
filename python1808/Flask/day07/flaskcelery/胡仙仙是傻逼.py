from celery import Celery

app = Celery("胡仙仙是傻逼",broker="redis://localhost:6379")

@app.task
def add(x,y):
    print(x+y)



if __name__ == "__main__":
    print("执行开始")
    add.delay(3,4)
    print("执行结束")