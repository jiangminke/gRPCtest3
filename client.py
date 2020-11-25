# coding:utf-8

import grpc
import hello_grpc1_pb2 as pb2
import hello_grpc1_pb2_grpc as pb2_grpc
import time
import random
##注意客户端只引入了pb2和pb2_grpc所以使用client.HelloDewei会把数据传入到
def test():
    index=0
    while 1:
        time.sleep(1)
        data =str(random.random())
        if index ==5:
            break
        print(index)
        index+=1
        yield pb2.TestClientsendStreamRequest(data=data)
def run():
    conn =grpc.insecure_channel('127.0.0.1:5000')#定义一个频道，访问本地ip
    client = pb2_grpc.BilibiliStub(channel=conn)
    #unary #response=client.HelloDewei(pb2.HelloDeweiReq(name='dewei',age=33))##必须传入这个格式
    #unary #print(response.result)

    '''
    抛异常
    try:
        response = client.HelloDewei(pb2.HelloDeweiReq(name='dewei', age=33))  ##必须传入这个格式
        print(response.result)
    except Exception as e:
        #print(dir(e))#这个能看到e中有哪些数据，就是哪些异常，这里面有code和detail，对应了服务器的set_code 和set_details
        print(e.code().name,e.code().value)#第一个是错误码
        print(e.details())
    '''


    #单#response=client.TestClientRecvStream(pb2.TestClientRecvStreamRequest(data='dewei'))

    #单#for item in response:##客户端不停接受流的形式，不停循环这个状态
    #单#    print(item.result)

    #双#response = client.TestTwoWayStream(test())#这里是有一个超时机制的（就是请求时间太长，服务器无回复）timeout形参超过deadlin就直接抛出异常结束掉
    #双#for res in response:
    #双#   print(res.result)

    response, call = client.HelloDewei.with_call(pb2.HelloDeweiReq(name='dewei', age=33),compression=grpc.Compression.Gzip,
                                                 metadata=(('nam','dewe'),)#必须使用service里面的认证用户，否则是错的'name','dewei'
                                                 )#这里必须',',否则就是错的
    print(response.result)
    print(call.trailing_metadata())
    headers=call.trailing_metadata()
    print(headers[0][1])
    #print(dir(headers[0][1]))#用dir表示这个里面有哪些参数
    print(headers[0].key,headers[0].value)




if __name__ == '__main__':
    run()

