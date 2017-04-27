//
//  PythonModule.h
//  OC-Python
//
//  Created by youzu on 2017/3/22.
//  Copyright © 2017年 mob. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface PythonModule : NSObject

/**
 获取单例对象

 @return 单例对象
 */
+ (instancetype)sharedInstance;

/**
 OC初始化Python模块
 
 @param argc 参数个数
 @param argv 参数值
 */
- (void)initModuleWithArgc:(int)argc argv:(const char *[])argv;

/**
 OC 调用 Python
 
 @param funcKey 函数名称
 @param args 函数参数
 @return 返回值
 */
- (NSString *)pyCallWithFunctionKey:(NSString *)funcKey Args:(NSString *)args;

@end
