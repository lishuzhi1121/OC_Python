//
//  PythonModule.m
//  OC-Python
//
//  Created by youzu on 2017/3/22.
//  Copyright © 2017年 mob. All rights reserved.
//

#import "PythonModule.h"
#import <Cocoa/Cocoa.h>
#import <Python/Python.h>

/**
 函数声明
 */
static PyObject *myLog(PyObject *self, PyObject *args);
static PyObject *myAlert(PyObject *self, PyObject *args);


@implementation PythonModule

/**
 获取单例对象
 
 @return 单例对象
 */
+ (instancetype)sharedInstance
{
    static PythonModule *_module = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        _module = [[PythonModule alloc] init];
    });
    return _module;
}


/**
 OC初始化Python模块

 @param argc 参数个数
 @param argv 参数值
 */
- (void)initModuleWithArgc:(int)argc argv:(const char *[])argv
{
    //bundle资源路径
    NSString *resourcePath = [[NSBundle mainBundle] pathForResource:@"OC_Python_Script" ofType:@"bundle"];
    //python路径组成数组
    NSArray *pythonPathArray = [NSArray arrayWithObjects:resourcePath, [resourcePath stringByAppendingPathComponent:@" "], [resourcePath stringByAppendingPathComponent:@"Python"], nil];
    //设置python环境变量（包含项目资源文件目录、其他python文件引用目录【重要，否则提示"ImportError: No module named"等错误】）
    /*
     函数说明: setenv()用来改变或增加环境变量的内容。
     参数说明: name 为环境变量名称字符串。
             value 则为变量内容
             overwrite 用来决定是否要改变已存在的环境变量。如果没有此环境变量则无论overwrite为何值均添加此环境变量。
             若环境变量存在，当overwrite不为0时，原内容会被改为参数value所指的变量内容；当overwrite为0时，则参数value会被忽略。
             返回值 执行成功则返回0，有错误发生时返回-1。
     */
    int setenvRes = setenv("PYTHONPATH", [[pythonPathArray componentsJoinedByString:@":"] UTF8String], 1);
    
    if (setenvRes != 0)
    {
        NSLog(@"Setenv PythonPath Error!");
        return;
    }
    
    //设置Python启动路径
    Py_SetProgramName("/usr/bin/python");
    
    //调用系统初始化
    Py_Initialize();
    
    //设置参数
    PySys_SetArgv(argc, (char **)argv);
    
    //模块初始化
    initoc_python_module();
    
    //导入引用模块
    PyImport_ImportModule("PBXProjectHelper");
    
    NSBundle *scriptBundle = [NSBundle bundleWithPath:[[NSBundle mainBundle] pathForResource:@"OC_Python_Script" ofType:@"bundle"]];
    //Main.py 文件路径
    NSString *mainPath = [scriptBundle pathForResource:@"Main" ofType:@"py" inDirectory:@"Python"];
    
    FILE *mainFile = fopen([mainPath UTF8String], "r");
    int result = PyRun_SimpleFile(mainFile, [[mainPath lastPathComponent] UTF8String]);
    
    if (result != 0)
    {
        NSAlert *alert = [[NSAlert alloc] init];
        [alert setMessageText:@"Run Main.py Error!"];
        [alert runModal];
    }
    
    //释放Python对象
    Py_Finalize();
//    free(argv);
}


/**
 声明该模块具有哪些方法,即在Python中执行到这些函数时都会回调这里对应的方法
 PyMethodDef结构体有四个字段:
 第一个是一个字符串，表示在Python中对应的方法的名称；
 第二个是对应的OC代码的方法；
 第三个是一个标识位，表示该Python方法是否需要参数，METH_NOARGS表示不需要参数，METH_VARARGS表示需要参数；
 第四个是一个字符串，它是该方法的__doc__属性，这个不是必须的，可以为NULL。
 */
static PyMethodDef oc_python_module_methods[] = {
    {"myLog", myLog, METH_VARARGS, NULL},
    {"myAlert", myAlert, METH_NOARGS, NULL}
};

//static PyModuleDef oc_python_module = {
//    PyModuleDef_HEAD_INIT,
//    //模块名称
//    "oc_python_module",
//    //模块描述,可以是NULL
//    NULL,
//    //模块解释器状态范围,如果是-1则保持全局状态
//    -1,
//    //通过PyMethodDef定义的模块方法表指针,如果没有方法可以是NULL
//    oc_python_module_methods
//};

/**
 模块初始化,即是在第一次使用import语句导入模块时会执行
 这是Python 2的写法：
    函数名必须为initmodule_name这样的格式,例如我们的module名为oc_python_module,所以函数名就是initoc_python_module.
 */
PyMODINIT_FUNC
initoc_python_module(void)
{
    Py_InitModule("oc_python_module", oc_python_module_methods);
}

/**
 模块初始化,即是在第一次使用import语句导入模块时会执行
 这是Python 3的写法：
    函数名必须为PyInit_module_name这样的格式,例如我们的module名为oc_python_module,所以函数名就是PyInit_oc_python_module.
 */
//PyMODINIT_FUNC
//PyInit_oc_python_module(void)
//{
//    return PyModule_Create(&oc_python_module);
//}


/**
 打印日志

 @param self 模块对象
 @param args 参数
 @return PyObject对象
 */
static PyObject *myLog(PyObject *self, PyObject *args)
{
    const char *command;
    if (!PyArg_ParseTuple(args, "z", &command))
    {
        return NULL;
    }
    
    NSString *pyStr = [NSString stringWithUTF8String:command];
    NSLog(@"%@", pyStr);
    
    Py_IncRef(Py_None);
    return Py_None;
}


/**
 弹窗提示

 @param self 模块对象
 @return PyObject对象
 */
static PyObject *myAlert(PyObject *self, PyObject *args)
{
    NSAlert *alert = [[NSAlert alloc] init];
    alert.messageText = @"I'm alert from Python!";
    [alert runModal];
    
    Py_IncRef(Py_None);
    return Py_None;
}

/**
 OC 调用 Python

 @param funcKey 函数名称
 @param args 函数参数数组(当前配置为数组中只能有3个元素)
 @return 返回值
 */
- (NSString *)pyCallWithFunctionKey:(NSString *)funcKey Args:(NSArray<NSString *> *)args
{
    PyObject *pName, *pModule, *pFunc, *pValue = NULL, *pResult=NULL;
    //初始化Python解释器
    Py_Initialize();
    
    //模块初始化
    initoc_python_module();
    
    //获取内置在Python的名称对象
    pName = PyString_FromString((char *)"PBXProjectHelper");
    
    //加载模块对象
    pModule = PyImport_Import(pName);
    
    //获取模块中的函数
    pFunc = PyObject_GetAttrString(pModule, [funcKey UTF8String]);
    
    //判断能否被执行
    if (PyCallable_Check(pFunc))
    {
        if (args.count > 0) {
            NSUInteger argc = args.count;
            NSMutableString *mStr = [NSMutableString stringWithCapacity:3];
            for (int i = 0; i < argc; i++)
            {
                [mStr appendString:@"z"];
            }
            NSLog(@"---> mStr: %@", mStr);
            
            //设置函数参数
            pValue = Py_BuildValue([mStr UTF8String], [args.firstObject UTF8String], [args[1] UTF8String]);
            PyErr_Print();
            
            //调用函数
            pResult = PyObject_CallObject(pFunc, pValue);
            PyErr_Print();
        }
        else
        {
            pResult = PyObject_CallObject(pFunc, NULL);
            PyErr_Print();
        }
    }
    else
    {
        PyErr_Print();
    }
    
    //释放对象
    if (pValue)
    {
        Py_DECREF(pValue);
    }
    Py_DECREF(pFunc);
    Py_DECREF(pModule);
    Py_DECREF(pName);
    
    //Python解释器完成
    Py_Finalize();
    
    //结果处理
    if (PyString_Check(pResult))
    {
        //如果是PyString就转成NSString返回
        return [NSString stringWithUTF8String:PyString_AsString(pResult)];
    }
    else if (PyInt_Check(pResult))
    {
        //否则就认为是Pyint转成long之后再转为NSString返回
        return [NSString stringWithFormat:@"%ld", PyInt_AsLong(pResult)];
    }
    else
    {
        NSDictionary *paramsDic = @{@"success":@"yes", @"msg":@"Python return value type unknown."};
        NSError *dataError = nil;
        NSData *data = [NSJSONSerialization dataWithJSONObject:paramsDic options:NSJSONWritingPrettyPrinted error:&dataError];
        NSString *paramsStr = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
        return paramsStr;
    }
}







@end
