//
//  ViewController.m
//  OC-Python
//
//  Created by youzu on 2017/3/22.
//  Copyright © 2017年 mob. All rights reserved.
//

#import "ViewController.h"
#import "OperationManager.h"

//python 需要操作的文件路径
static NSString *const currentPath = @"/Users/lishuzhi/Desktop";

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];

    [self initPython];
}


- (void)initPython
{
    const char **argv = (const char **)malloc((currentPath.length + 1) * sizeof(char *));
    argv[0] = strdup([currentPath UTF8String]);
    
    [[OperationManager sharedManager] lauchPython:1 argv:argv];
}

- (IBAction)pythonLogButtonClick:(NSButton *)sender
{
    [[OperationManager sharedManager] pythonLog:@[@"Hello", @"World", @"!"]];
}

- (IBAction)pythonWirteFileButtonClick:(NSButton *)sender
{
    [[OperationManager sharedManager] pythonWriteFile];
}

- (IBAction)ocLogButtonClick:(NSButton *)sender
{
    [[OperationManager sharedManager] ocLog];
}

- (IBAction)ocAlertButtonClick:(NSButton *)sender
{
    [[OperationManager sharedManager] ocAlert];
}


@end
