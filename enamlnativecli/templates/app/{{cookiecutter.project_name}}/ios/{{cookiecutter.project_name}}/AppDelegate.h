//
//  AppDelegate.h
//  {{cookiecutter.app_name}}
//
//  Copyright © 2018 {{cookiecutter.author}}. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface AppDelegate : UIResponder <UIApplicationDelegate>

@property (strong, nonatomic) UIWindow *window;

-(int)startPython:(UIApplication *)application;
-(void)stopPython:(UIApplication *)application;

@end

