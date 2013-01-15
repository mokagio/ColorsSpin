//
//  ViewController.m
//  ColorSpin
//
//  Created by Giovanni Lodi on 1/6/13.
//  Copyright (c) 2013 mokagio. All rights reserved.
//

#import "ViewController.h"
#import "UIColor+CSSColors.h"

@interface ViewController ()
- (void)spinColor;
- (UIColor *)getRandomColor;
@end

@implementation ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];

    UITapGestureRecognizer *tapRecognizer = [[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(spinColor)];
    tapRecognizer.numberOfTapsRequired = 1;
    
    [self.view addGestureRecognizer:tapRecognizer];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (void)spinColor
{
    [self.view setBackgroundColor:[self getRandomColor]];
}

- (UIColor *)getRandomColor
{
    int random = arc4random() % 6;
    
    UIColor *color = nil;
    
    switch (random) {
        case 0:
            color = [UIColor lightSeaGreenColor];
            break;
        case 1:
            // dunno why, but indianRedColor reminds me of Assassin's Creed Brotherhood
            color = [UIColor indianRedColor];
            break;
        case 2:
            color = [UIColor yellowGreenColor];
            break;
        case 3:
            color = [UIColor gainsboroColor];
            break;
        case 4:
            color = [UIColor midnightBlueColor];
            break;
        case 5:
            color = [UIColor orchidColor];
            break;
        default:
            color = [UIColor ghostWhiteColor];
            break;
    }
    
    return color;
}


@end
