//
//  OperationManager.m
//  OC-Python
//
//  Created by youzu on 2017/3/23.
//  Copyright © 2017年 mob. All rights reserved.
//

#import "OperationManager.h"
#import "PythonModule.h"

@implementation OperationManager

/**
 获取单例对象
 
 @return 单例对象
 */
+ (instancetype)sharedManager
{
    static OperationManager *_manager = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        _manager = [[OperationManager alloc] init];
    });
    return _manager;
}

/**
 启动 Python,初始化

 @param argc 参数个数
 @param argv 参数值
 */
- (void)lauchPython:(int)argc argv:(const char *[])argv
{
    [[PythonModule sharedInstance] initModuleWithArgc:argc argv:argv];
}


/**
 OC 调用 Python 输出字符串

 @param args 参数数组
 */
- (void)pythonLog:(NSArray<NSString *> *)args
{
    [self _operationWithFunctionKey:@"oc_PythonLogButtonClick" params:args];
}

/**
 OC 调用 Python 写文件
 */
- (void)pythonWriteFile
{
    [self _operationWithFunctionKey:@"oc_PythonWriteFileButtonClick" params:nil];
}


/**
 在 Python 中反射调用 OC 打印
 */
- (void)ocLog
{
    [self _operationWithFunctionKey:@"python_OCLogButtonClick" params:nil];
}

/**
 在 Python 中反射调用 OC 弹窗
 */
- (void)ocAlert
{
    [self _operationWithFunctionKey:@"python_OCAlertButtonClick" params:nil];
}

#pragma mark - Private

/**
 与 Python 模块交互方法

 @param funcKey 调用Python中的函数名
 @param params 函数参数数组(当前配置为数组中只能有3个元素)
 @return 返回值Json
 */
- (id)_operationWithFunctionKey:(NSString *)funcKey params:(NSArray<NSString *> *)params
{
    NSString *result = [[PythonModule sharedInstance] pyCallWithFunctionKey:funcKey Args:params];
    
    NSError *objectError = nil;
    return [NSJSONSerialization JSONObjectWithData:[result dataUsingEncoding:NSUTF8StringEncoding] options:NSJSONReadingMutableContainers error:&objectError];
}




@end
