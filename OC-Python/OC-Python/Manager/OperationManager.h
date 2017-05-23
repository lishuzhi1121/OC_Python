//
//  OperationManager.h
//  OC-Python
//
//  Created by youzu on 2017/3/23.
//  Copyright © 2017年 mob. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface OperationManager : NSObject

/**
 获取单例对象

 @return 单例对象
 */
+ (instancetype)sharedManager;

/**
 启动 Python,初始化
 
 @param argc 参数个数
 @param argv 参数值
 */
- (void)lauchPython:(int)argc argv:(const char *[])argv;

/**
 OC 调用 Python 输出字符串
 
 @param args 参数数组
 */
- (void)pythonLog:(NSArray<NSString *> *)args;

/**
 OC 调用 Python 写文件
 */
- (void)pythonWriteFile;

/**
 在 Python 中反射调用 OC 打印
 */
- (void)ocLog;

/**
 在 Python 中反射调用 OC 弹窗
 */
- (void)ocAlert;

@end
