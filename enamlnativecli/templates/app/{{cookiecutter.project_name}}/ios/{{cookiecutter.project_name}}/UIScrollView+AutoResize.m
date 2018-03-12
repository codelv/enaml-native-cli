//
//  UIScrollView+AutoResize.m
//  demo
//
//  Created by jrm on 8/27/17.
//  Copyright © 2017 frmdstryr. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "UIScrollView+AutoResize.h"
#import <UIKit/UIKit.h>



@implementation UIScrollView(AutoResize)

- (void) fitToContents {
    CGRect contentRect = CGRectZero;
    for (UIView* view in [self subviews]) {
        CGRectUnion(contentRect, view.frame);
    }
    self.contentSize = contentRect.size;
}

@end
