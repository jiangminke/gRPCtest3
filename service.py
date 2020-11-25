# coding:utf-8
import time#通常把内置的包放在最上面便于加载
'''
如果是python环境那么，导包会先从同级目录去找你导入的模块。如果找不到，回去python内置的第三方包去查找模块。
完整的查找方式为：同级方法<--同级模块<--同级包<--第三方包
'''

'''
客户端与服务端传输与接收headers：key value :在web开发中常见其实就是metadata元数据
客户端与服务端传输和接收数据进行压缩和解压缩，只需要写服务端和客户端写压缩，解压缩会自动处理
重点（坑）：grpc当数据发送量超过2M会报错，当需要更大的流量的时候，需要配置一下
'''

'''
grpc服务端书写一个拦截器：用于验证身份和授权。如果是链路只需要拿到用户的相关信息记录下来就行，如果是验证身份则需要返回给用户一些错误信息
init、code（错误信息）、detail
grpc_code：返回错误的错误函数，例如验证失败，就终止本次操作，abort发送给客户端错误码
intercept——service（self，continuation，headler_call_details）
'''


import grpc
import hello_grpc1_pb2 as pb2
import hello_grpc1_pb2_grpc as pb2_grpc
from concurrent import futures#创建线程数量

def _abort(code,details):
    def terminate(ignored_request,context):#函数里面闭包函数，也就是装饰器
        context.abort(code,details)
    return grpc.unary_unary_rpc_method_handler(terminate)#这里不能用terminate（）
class Testinterceptor(grpc.ServerInterceptor):
    def __init__(self,key,value,code,detail):
        self.key=key
        self.value=value
        self._abort=_abort(code,detail)

    def intercept_service(self, continuation, handler_call_details):#这相当于是虚函数，继承自grpc.ServerInterceptor，修改他
        #continuation函数执行器
        #handler_call_details header
        headers=dict(handler_call_details.invocation_metadata)#把metadata元组变为字典
        print(headers)
        print(handler_call_details.invocation_metadata)
        print(self.value)
        #print(headers.get(self.key,'meiyou'))#查找header中是不是有dewei如果没有就返回'meiyou'
        if headers.get(self.key,'') != self.value:#查找header中是不是有dewei如果没有就返回''
            return self._abort
        return continuation(handler_call_details)#这里的headers应该就是客户端的验证信息



class Bilibili(pb2_grpc.BilibiliServicer):#Bilibili是proto文件里的service，用了里面的一个服务
    def HelloDewei(self,request,context):#这里的context应该是返回给客户端的，是客户端和服务器可以共用的变量
        name=request.name
        age=request.age
        '''
        抛异常
        context.set_details('haha')
        context.set_code(grpc.StatusCode.DATA_LOSS)
        raise context
        '''

        context.set_trailing_metadata((('name','dewei'),('key','value')))#通过这函数吧这些数据返回给了发送给客户端的headers
        headers=context.invocation_metadata()
        print(headers)
        print(headers[0].key, headers[0].value)

        result=f'my name is {name}, i am {age} years old'
        context.set_compression(grpc.Compression.Gzip)#压缩，只需要服务器压缩，之后客户端会自动解压缩
        return pb2.HelloDeweiReply(result=result)

    def TestClientRecvStream(self, request, context):
        index=0
        while context.is_active():##监听客户端是不是一个活跃的客户端，如果是活跃的状态就会不断发送数据
            data=request.data
            time.sleep(1)
            index +=1
            yield pb2.TestClientRecvStreamResponse(result='send %d %s' %(index,data))#yiel表示返回，由于我们是需要传输流所以不能用return
            #这里就是response我们操作之后的数据，，例如我们可以输入单词，然后返回查询到的词向量放入这里

    def TestClientsendStream(self, request_iterator, context):
        for request in request_iterator:
            print(request.data)
            return pb2.TestClientRecvStreamResponse(result='ok')

    def TestTwoWayStream(self,request_iterator, context):
        index=0
        for request in request_iterator:
            data=request.data
            if index==3:#当客户端发送3次之后就强制关闭
                #context.cancel()#也可以使用break跳出for循环比较友好
                break
            index +=1
            yield pb2.TestTwoWayStreamResponse(result='service send client %s' %data)
        print("强制断开用户xxxx")#断开之后服务器仍然在运行


def run():
    validator=Testinterceptor(key='name',value='dewei',code=grpc.StatusCode.UNAUTHENTICATED,detail='Access denied+failed')#验证,输入姓名和关键字，以及身份验证码错误的code
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=4),
                              compression=grpc.Compression.Gzip,
                              options=[('grpc.max_send_message_length',50*1024*1024),('grpc.max_receive_message_length',50*1024*1024)],
                              interceptors=(validator,),)#最大4个线程,options=支持客户端发送的最大的流量,intercepters是使用拦截器可以有多个
    #50*1024*1024表示50M
   # grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=4),compression=grpc.Compression.Gzip)#实现服务器端所有函数都可以压缩
    pb2_grpc.add_BilibiliServicer_to_server(Bilibili(),grpc_server)#把Bilibili这个类注册到grpc_server
    grpc_server.add_insecure_port('0.0.0.0:5000')#绑定ip和5000端口,表示所有ip都可以访问
    print('server will start at 0.0.0.0:5000')#以后可以动态的去绑定端口
    grpc_server.start()#如果只用start则服务启动一次就结束了，我们需要他一直启动着，就是监听

    try:
        while(1):
            time.sleep(3600)
    #except KeyboardInterrupt:  将无法捕获
    except KeyboardInterrupt as e:#如果键盘或鼠标使用了ctrl+c或者delete，这里好像在python3中无法捕获该异常了
        #由于KeyboardInterrupt和except 继承了同一个父类所以无法捕获
        print('exit')
        grpc_server.stop(0)#安全退出



if __name__ == '__main__':
    run()
