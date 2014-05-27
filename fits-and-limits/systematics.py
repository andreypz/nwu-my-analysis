#!/usr/bin/env python
from collections import defaultdict
import numpy as np
cs_gg  = np.array([20.86, 19.27, 17.85, 16.57, 15.42, 14.46, 13.55], float)
cs_vbf = np.array([1.649,1.578,1.511,1.448,1.389,1.333,1.280], float)
cs_Wh  = np.array([0.8052,0.7046,0.6169,0.5416,0.4768,0.4216,0.3728],float)
cs_Zh  = np.array([0.4710,0.4153,0.3671,0.3259,0.2899,0.2583,0.2308],float)
cs_Vh  = np.sum([cs_Wh, cs_Zh], axis=0)

cs_tot = cs_gg+cs_vbf+cs_Wh+cs_Zh
print 'Higgs cross sections total:\n',cs_tot
BR_mu  = np.array([ 3.77201342e-05, 3.91992735e-05, 3.91260504e-05,
                    3.70906457e-05, 3.37937743e-05, 2.95381743e-05,
                    2.42427306e-05])

pdf_gg = defaultdict(dict)

pdf_gg['2012'] = {'120.0': '0.931/1.075',
                  '120.5': '0.931/1.075',
                  '121.0': '0.931/1.075',
                  '121.5': '0.931/1.075',
                  '122.0': '0.931/1.075',
 '122.5': '0.931/1.075',
 '123.0': '0.931/1.075',
 '123.5': '0.931/1.075',
 '124.0': '0.931/1.075',
 '124.5': '0.931/1.075',
 '125.0': '0.931/1.075',
 '125.5': '0.931/1.075',
 '126.0': '0.931/1.075',
 '126.5': '0.931/1.075',
 '127.0': '0.931/1.075',
 '127.5': '0.931/1.075',
 '128.0': '0.931/1.075',
 '128.5': '0.931/1.075',
 '129.0': '0.931/1.075',
 '129.5': '0.931/1.075',
 '130.0': '0.931/1.075',
 '130.5': '0.931/1.075',
 '131.0': '0.93/1.075',
 '131.5': '0.93/1.075',
 '132.0': '0.93/1.075',
 '132.5': '0.93/1.075',
 '133.0': '0.93/1.074',
 '133.5': '0.93/1.074',
 '134.0': '0.93/1.074',
 '134.5': '0.93/1.074',
 '135.0': '0.93/1.074',
 '135.5': '0.93/1.074',
 '136.0': '0.93/1.074',
 '136.5': '0.93/1.074',
 '137.0': '0.93/1.074',
 '137.5': '0.93/1.074',
 '138.0': '0.931/1.074',
 '138.5': '0.931/1.074',
 '139.0': '0.931/1.074',
 '139.5': '0.931/1.074',
 '140.0': '0.931/1.074',
 '141.0': '0.931/1.073',
 '142.0': '0.931/1.073',
 '143.0': '0.931/1.073',
 '144.0': '0.931/1.073',
 '145.0': '0.931/1.073',
 '146.0': '0.931/1.073',
 '147.0': '0.931/1.073',
 '148.0': '0.93/1.073',
 '149.0': '0.93/1.074',
 '150.0': '0.93/1.074',
 '151.0': '0.93/1.074',
 '152.0': '0.929/1.074',
 '153.0': '0.929/1.075',
 '154.0': '0.929/1.075',
 '155.0': '0.929/1.075',
 '156.0': '0.929/1.075',
 '157.0': '0.929/1.075',
 '158.0': '0.929/1.075',
 '159.0': '0.929/1.075',
 '160.0': '0.929/1.075'}

pdf_gg['2011'] = {'120.0': '0.921/1.072',
 '120.5': '0.9211/1.0719',
 '121.0': '0.9212/1.0717',
 '121.5': '0.9213/1.0716',
 '122.0': '0.9214/1.0715',
 '122.5': '0.9215/1.0714',
 '123.0': '0.9216/1.0713',
 '123.5': '0.9217/1.0712',
 '124.0': '0.9218/1.0711',
 '124.5': '0.9219/1.0711',
 '125.0': '0.922/1.071',
 '125.5': '0.9221/1.0709',
 '126.0': '0.9222/1.0708',
 '126.5': '0.9223/1.0707',
 '127.0': '0.9224/1.0706',
 '127.5': '0.9225/1.0705',
 '128.0': '0.9226/1.0704',
 '128.5': '0.9227/1.0703',
 '129.0': '0.9228/1.0702',
 '129.5': '0.9229/1.0701',
 '130.0': '0.923/1.07',
 '130.5': '0.9231/1.0699',
 '131.0': '0.9232/1.0698',
 '131.5': '0.9233/1.0697',
 '132.0': '0.9234/1.0696',
 '132.5': '0.9235/1.0695',
 '133.0': '0.9236/1.0694',
 '133.5': '0.9237/1.0693',
 '134.0': '0.9238/1.0692',
 '134.5': '0.9239/1.0691',
 '135.0': '0.924/1.069',
 '135.5': '0.9241/1.0689',
 '136.0': '0.9242/1.0688',
 '136.5': '0.9243/1.0687',
 '137.0': '0.9244/1.0686',
 '137.5': '0.9245/1.0685',
 '138.0': '0.9246/1.0684',
 '138.5': '0.9247/1.0683',
 '139.0': '0.9248/1.0682',
 '139.5': '0.9249/1.0681',
 '140.0': '0.925/1.068',
 '141.0': '0.9251/1.0678',
 '142.0': '0.9251/1.0676',
 '143.0': '0.9251/1.0674',
 '144.0': '0.9251/1.0672',
 '145.0': '0.925/1.067',
 '146.0': '0.9251/1.0668',
 '147.0': '0.9253/1.0666',
 '148.0': '0.9255/1.0664',
 '149.0': '0.9257/1.0662',
 '150.0': '0.926/1.066',
 '151.0': '0.9262/1.0658',
 '152.0': '0.9264/1.0656',
 '153.0': '0.9266/1.0654',
 '154.0': '0.9268/1.0652',
 '155.0': '0.927/1.065',
 '156.0': '0.9272/1.0648',
 '157.0': '0.9274/1.0646',
 '158.0': '0.9276/1.0644',
 '159.0': '0.9278/1.0642',
 '160.0': '0.928/1.064'}

pdf_tth = defaultdict(dict)
pdf_tth['2012'] = {'120.0': '0.907/1.039',
 '120.5': '0.907/1.039',
 '121.0': '0.907/1.039',
 '121.5': '0.907/1.039',
 '122.0': '0.907/1.039',
 '122.5': '0.907/1.039',
 '123.0': '0.907/1.038',
 '123.5': '0.907/1.038',
 '124.0': '0.907/1.038',
 '124.5': '0.907/1.038',
 '125.0': '0.907/1.038',
 '125.5': '0.907/1.038',
 '126.0': '0.907/1.038',
 '126.5': '0.907/1.038',
 '127.0': '0.907/1.038',
 '127.5': '0.907/1.038',
 '128.0': '0.907/1.037',
 '128.5': '0.907/1.037',
 '129.0': '0.907/1.037',
 '129.5': '0.907/1.037',
 '130.0': '0.907/1.037',
 '130.5': '0.907/1.037',
 '131.0': '0.907/1.037',
 '131.5': '0.907/1.037',
 '132.0': '0.907/1.037',
 '132.5': '0.908/1.037',
 '133.0': '0.908/1.037',
 '133.5': '0.908/1.037',
 '134.0': '0.908/1.037',
 '134.5': '0.908/1.037',
 '135.0': '0.908/1.037',
 '135.5': '0.908/1.037',
 '136.0': '0.908/1.037',
 '136.5': '0.908/1.037',
 '137.0': '0.908/1.037',
 '137.5': '0.908/1.037',
 '138.0': '0.908/1.036',
 '138.5': '0.908/1.036',
 '139.0': '0.908/1.036',
 '139.5': '0.908/1.036',
 '140.0': '0.908/1.036',
 '140.5': '0.908/1.036',
 '141.0': '0.908/1.036',
 '141.5': '0.908/1.036',
 '142.0': '0.908/1.036',
 '142.5': '0.908/1.036',
 '143.0': '0.908/1.035',
 '143.5': '0.908/1.035',
 '144.0': '0.908/1.035',
 '144.5': '0.908/1.035',
 '145.0': '0.908/1.035',
 '145.5': '0.908/1.035',
 '146.0': '0.908/1.035',
 '146.5': '0.908/1.035',
 '147.0': '0.908/1.035',
 '147.5': '0.908/1.035',
 '148.0': '0.909/1.035',
 '148.5': '0.909/1.035',
 '149.0': '0.909/1.035',
 '149.5': '0.909/1.035',
 '150.0': '0.909/1.035',
 '151.0': '0.909/1.035',
 '152.0': '0.909/1.035',
 '153.0': '0.909/1.034',
 '154.0': '0.909/1.034',
 '155.0': '0.909/1.034',
 '156.0': '0.909/1.034',
 '157.0': '0.909/1.034',
 '158.0': '0.909/1.034',
 '159.0': '0.909/1.034',
 '160.0': '0.909/1.034'}

pdf_tth['2011'] = {'120.0': '0.906/1.034',
 '120.5': '0.906/1.034',
 '121.0': '0.906/1.034',
 '121.5': '0.906/1.034',
 '122.0': '0.906/1.034',
 '122.5': '0.906/1.033',
 '123.0': '0.907/1.033',
 '123.5': '0.907/1.033',
 '124.0': '0.907/1.033',
 '124.5': '0.907/1.033',
 '125.0': '0.907/1.033',
 '125.5': '0.907/1.033',
 '126.0': '0.907/1.033',
 '126.5': '0.907/1.033',
 '127.0': '0.907/1.033',
 '127.5': '0.907/1.032',
 '128.0': '0.907/1.032',
 '128.5': '0.907/1.032',
 '129.0': '0.907/1.032',
 '129.5': '0.907/1.032',
 '130.0': '0.907/1.032',
 '130.5': '0.907/1.032',
 '131.0': '0.907/1.032',
 '131.5': '0.907/1.032',
 '132.0': '0.907/1.032',
 '132.5': '0.908/1.032',
 '133.0': '0.908/1.031',
 '133.5': '0.908/1.031',
 '134.0': '0.908/1.031',
 '134.5': '0.908/1.031',
 '135.0': '0.908/1.031',
 '135.5': '0.908/1.031',
 '136.0': '0.908/1.031',
 '136.5': '0.908/1.031',
 '137.0': '0.908/1.031',
 '137.5': '0.908/1.03',
 '138.0': '0.908/1.03',
 '138.5': '0.908/1.03',
 '139.0': '0.908/1.03',
 '139.5': '0.908/1.03',
 '140.0': '0.908/1.03',
 '141.0': '0.908/1.03',
 '142.0': '0.908/1.03',
 '143.0': '0.909/1.029',
 '144.0': '0.909/1.029',
 '145.0': '0.909/1.029',
 '146.0': '0.909/1.029',
 '147.0': '0.909/1.029',
 '148.0': '0.909/1.029',
 '149.0': '0.909/1.029',
 '150.0': '0.909/1.029',
 '151.0': '0.909/1.029',
 '152.0': '0.909/1.029',
 '153.0': '0.909/1.028',
 '154.0': '0.909/1.028',
 '155.0': '0.909/1.028',
 '156.0': '0.909/1.028',
 '157.0': '0.909/1.028',
 '158.0': '0.909/1.028',
 '159.0': '0.909/1.028',
 '160.0': '0.909/1.028'}

pdf_vbf = defaultdict(dict)
pdf_vbf['2012'] = {'120.0': '0.998/1.002',
 '120.5': '0.999/1.002',
 '121.0': '0.998/1.002',
 '121.5': '0.998/1.002',
 '122.0': '0.998/1.003',
 '122.5': '0.998/1.002',
 '123.0': '0.998/1.002',
 '123.5': '0.998/1.002',
 '124.0': '0.998/1.003',
 '124.5': '0.998/1.002',
 '125.0': '0.998/1.002',
 '125.5': '0.998/1.002',
 '126.0': '0.999/1.003',
 '126.5': '0.998/1.002',
 '127.0': '0.998/1.003',
 '127.5': '0.998/1.002',
 '128.0': '0.998/1.002',
 '128.5': '0.998/1.002',
 '129.0': '0.998/1.002',
 '129.5': '0.998/1.002',
 '130.0': '0.998/1.002',
 '130.5': '0.998/1.002',
 '131.0': '0.998/1.002',
 '131.5': '0.998/1.002',
 '132.0': '0.999/1.002',
 '132.5': '0.998/1.002',
 '133.0': '0.998/1.002',
 '133.5': '0.998/1.002',
 '134.0': '0.998/1.002',
 '134.5': '0.998/1.002',
 '135.0': '0.998/1.002',
 '135.5': '0.998/1.002',
 '136.0': '0.998/1.003',
 '136.5': '0.998/1.002',
 '137.0': '0.998/1.002',
 '137.5': '0.998/1.002',
 '138.0': '0.998/1.002',
 '138.5': '0.998/1.002',
 '139.0': '0.998/1.002',
 '139.5': '0.998/1.002',
 '140.0': '0.998/1.002',
 '141.0': '0.998/1.002',
 '142.0': '0.998/1.002',
 '143.0': '0.998/1.002',
 '144.0': '0.998/1.002',
 '145.0': '0.999/1.003',
 '146.0': '0.999/1.002',
 '147.0': '0.999/1.002',
 '148.0': '0.999/1.003',
 '149.0': '0.999/1.002',
 '150.0': '0.998/1.003',
 '151.0': '0.998/1.002',
 '152.0': '0.999/1.002',
 '153.0': '0.999/1.003',
 '154.0': '0.999/1.002',
 '155.0': '0.998/1.002',
 '156.0': '0.999/1.002',
 '157.0': '0.998/1.002',
 '158.0': '0.998/1.002',
 '159.0': '0.999/1.003',
 '160.0': '0.999/1.002'}

pdf_vbf['2011'] = {'120.0': '0.996/1.003',
 '120.5': '0.997/1.003',
 '121.0': '0.997/1.003',
 '121.5': '0.997/1.003',
 '122.0': '0.997/1.003',
 '122.5': '0.997/1.003',
 '123.0': '0.997/1.003',
 '123.5': '0.997/1.003',
 '124.0': '0.997/1.003',
 '124.5': '0.997/1.003',
 '125.0': '0.997/1.003',
 '125.5': '0.997/1.003',
 '126.0': '0.997/1.003',
 '126.5': '0.997/1.003',
 '127.0': '0.998/1.003',
 '127.5': '0.998/1.003',
 '128.0': '0.998/1.003',
 '128.5': '0.998/1.003',
 '129.0': '0.998/1.003',
 '129.5': '0.998/1.003',
 '130.0': '0.998/1.003',
 '130.5': '0.998/1.003',
 '131.0': '0.998/1.003',
 '131.5': '0.998/1.004',
 '132.0': '0.998/1.004',
 '132.5': '0.998/1.004',
 '133.0': '0.999/1.004',
 '133.5': '0.999/1.004',
 '134.0': '0.999/1.004',
 '134.5': '0.999/1.004',
 '135.0': '0.999/1.005',
 '135.5': '0.999/1.004',
 '136.0': '0.999/1.004',
 '136.5': '0.999/1.004',
 '137.0': '0.999/1.004',
 '137.5': '0.999/1.003',
 '138.0': '0.999/1.003',
 '138.5': '0.999/1.003',
 '139.0': '0.999/1.002',
 '139.5': '0.998/1.002',
 '140.0': '0.998/1.002',
 '141.0': '0.999/1.002',
 '142.0': '0.999/1.003',
 '143.0': '0.999/1.003',
 '144.0': '0.999/1.004',
 '145.0': '1/1.004',
 '146.0': '0.999/1.004',
 '147.0': '0.999/1.003',
 '148.0': '0.999/1.003',
 '149.0': '0.999/1.003',
 '150.0': '0.999/1.002',
 '151.0': '0.999/1.002',
 '152.0': '0.999/1.003',
 '153.0': '0.999/1.003',
 '154.0': '0.999/1.003',
 '155.0': '1/1.003',
 '156.0': '0.999/1.003',
 '157.0': '0.999/1.002',
 '158.0': '0.999/1.002',
 '159.0': '0.998/1.001',
 '160.0': '0.998/1.001'}

pdf_wh= defaultdict(dict)
pdf_wh['2012'] = {'120.0': '0.994/1.001',
 '120.5': '0.994/1.001',
 '121.0': '0.994/1.001',
 '121.5': '0.994/1.001',
 '122.0': '0.994/1.001',
 '122.5': '0.994/1.002',
 '123.0': '0.994/1.002',
 '123.5': '0.994/1.002',
 '124.0': '0.994/1.002',
 '124.5': '0.994/1.002',
 '125.0': '0.994/1.002',
 '125.5': '0.994/1.002',
 '126.0': '0.994/1.002',
 '126.5': '0.994/1.002',
 '127.0': '0.994/1.002',
 '127.5': '0.994/1.002',
 '128.0': '0.993/1.002',
 '128.5': '0.993/1.002',
 '129.0': '0.994/1.002',
 '129.5': '0.994/1.002',
 '130.0': '0.994/1.002',
 '130.5': '0.994/1.002',
 '131.0': '0.994/1.002',
 '131.5': '0.994/1.002',
 '132.0': '0.994/1.002',
 '132.5': '0.994/1.002',
 '133.0': '0.994/1.002',
 '133.5': '0.994/1.002',
 '134.0': '0.994/1.001',
 '134.5': '0.993/1.001',
 '135.0': '0.993/1.001',
 '135.5': '0.993/1.001',
 '136.0': '0.993/1.001',
 '136.5': '0.993/1.001',
 '137.0': '0.993/1.001',
 '137.5': '0.993/1.001',
 '138.0': '0.993/1.001',
 '138.5': '0.993/1.001',
 '139.0': '0.993/1.001',
 '139.5': '0.993/1.001',
 '140.0': '0.993/1.001',
 '141.0': '0.993/1.001',
 '142.0': '0.993/1.001',
 '143.0': '0.993/1.001',
 '144.0': '0.993/1.001',
 '145.0': '0.993/1.001',
 '146.0': '0.993/1.001',
 '147.0': '0.993/1.001',
 '148.0': '0.993/1.001',
 '149.0': '0.993/1.001',
 '150.0': '0.993/1.001',
 '151.0': '0.993/1.001',
 '152.0': '0.993/1.001',
 '153.0': '0.993/1.001',
 '154.0': '0.993/1.001',
 '155.0': '0.993/1.002',
 '156.0': '0.993/1.002',
 '157.0': '0.993/1.002',
 '158.0': '0.993/1.002',
 '159.0': '0.993/1.002',
 '160.0': '0.993/1.002'}

pdf_wh['2011'] = {'120.0': '0.993/1.004',
 '120.5': '0.993/1.004',
 '121.0': '0.993/1.004',
 '121.5': '0.993/1.003',
 '122.0': '0.993/1.003',
 '122.5': '0.992/1.003',
 '123.0': '0.992/1.003',
 '123.5': '0.992/1.003',
 '124.0': '0.992/1.002',
 '124.5': '0.992/1.002',
 '125.0': '0.992/1.002',
 '125.5': '0.992/1.002',
 '126.0': '0.992/1.002',
 '126.5': '0.992/1.002',
 '127.0': '0.992/1.002',
 '127.5': '0.992/1.002',
 '128.0': '0.992/1.003',
 '128.5': '0.992/1.003',
 '129.0': '0.992/1.003',
 '129.5': '0.992/1.003',
 '130.0': '0.992/1.003',
 '130.5': '0.992/1.003',
 '131.0': '0.993/1.004',
 '131.5': '0.993/1.004',
 '132.0': '0.994/1.005',
 '132.5': '0.994/1.005',
 '133.0': '0.994/1.005',
 '133.5': '0.995/1.006',
 '134.0': '0.995/1.006',
 '134.5': '0.996/1.007',
 '135.0': '0.996/1.007',
 '135.5': '0.996/1.007',
 '136.0': '0.996/1.007',
 '136.5': '0.996/1.006',
 '137.0': '0.996/1.006',
 '137.5': '0.996/1.006',
 '138.0': '0.995/1.006',
 '138.5': '0.995/1.006',
 '139.0': '0.995/1.005',
 '139.5': '0.995/1.005',
 '140.0': '0.995/1.005',
 '141.0': '0.994/1.004',
 '142.0': '0.994/1.004',
 '143.0': '0.993/1.003',
 '144.0': '0.993/1.003',
 '145.0': '0.992/1.002',
 '146.0': '0.992/1.002',
 '147.0': '0.992/1.003',
 '148.0': '0.992/1.003',
 '149.0': '0.992/1.004',
 '150.0': '0.992/1.004',
 '151.0': '0.992/1.004',
 '152.0': '0.992/1.004',
 '153.0': '0.992/1.005',
 '154.0': '0.992/1.005',
 '155.0': '0.992/1.005',
 '156.0': '0.992/1.005',
 '157.0': '0.992/1.005',
 '158.0': '0.993/1.005',
 '159.0': '0.993/1.005',
 '160.0': '0.993/1.005'}

pdf_zh = defaultdict(dict)
pdf_zh['2012'] = {'120.0': '0.986/1.015',
 '120.5': '0.986/1.015',
 '121.0': '0.986/1.015',
 '121.5': '0.986/1.015',
 '122.0': '0.986/1.015',
 '122.5': '0.985/1.015',
 '123.0': '0.985/1.016',
 '123.5': '0.985/1.016',
 '124.0': '0.985/1.016',
 '124.5': '0.985/1.016',
 '125.0': '0.985/1.016',
 '125.5': '0.985/1.016',
 '126.0': '0.985/1.016',
 '126.5': '0.985/1.016',
 '127.0': '0.985/1.016',
 '127.5': '0.985/1.016',
 '128.0': '0.985/1.017',
 '128.5': '0.985/1.017',
 '129.0': '0.985/1.017',
 '129.5': '0.984/1.017',
 '130.0': '0.984/1.017',
 '130.5': '0.984/1.017',
 '131.0': '0.984/1.017',
 '131.5': '0.984/1.017',
 '132.0': '0.984/1.017',
 '132.5': '0.984/1.017',
 '133.0': '0.984/1.018',
 '133.5': '0.984/1.018',
 '134.0': '0.984/1.018',
 '134.5': '0.984/1.018',
 '135.0': '0.984/1.018',
 '135.5': '0.984/1.018',
 '136.0': '0.983/1.018',
 '136.5': '0.983/1.018',
 '137.0': '0.983/1.018',
 '137.5': '0.983/1.019',
 '138.0': '0.983/1.019',
 '138.5': '0.983/1.019',
 '139.0': '0.983/1.019',
 '139.5': '0.983/1.019',
 '140.0': '0.983/1.019',
 '141.0': '0.983/1.019',
 '142.0': '0.983/1.019',
 '143.0': '0.982/1.020',
 '144.0': '0.982/1.020',
 '145.0': '0.982/1.020',
 '146.0': '0.982/1.020',
 '147.0': '0.982/1.021',
 '148.0': '0.982/1.021',
 '149.0': '0.982/1.021',
 '150.0': '0.982/1.021',
 '151.0': '0.982/1.022',
 '152.0': '0.982/1.022',
 '153.0': '0.982/1.022',
 '154.0': '0.981/1.022',
 '155.0': '0.981/1.022',
 '156.0': '0.981/1.023',
 '157.0': '0.981/1.023',
 '158.0': '0.981/1.023',
 '159.0': '0.981/1.024',
 '160.0': '0.981/1.024'}

pdf_zh['2011'] = {'120.0': '0.988/1.015',
 '120.5': '0.988/1.015',
 '121.0': '0.987/1.015',
 '121.5': '0.987/1.015',
 '122.0': '0.986/1.015',
 '122.5': '0.986/1.015',
 '123.0': '0.986/1.014',
 '123.5': '0.985/1.014',
 '124.0': '0.985/1.014',
 '124.5': '0.984/1.014',
 '125.0': '0.984/1.014',
 '125.5': '0.984/1.014',
 '126.0': '0.984/1.014',
 '126.5': '0.985/1.014',
 '127.0': '0.985/1.014',
 '127.5': '0.985/1.015',
 '128.0': '0.985/1.015',
 '128.5': '0.985/1.015',
 '129.0': '0.986/1.015',
 '129.5': '0.986/1.015',
 '130.0': '0.986/1.015',
 '130.5': '0.986/1.015',
 '131.0': '0.986/1.015',
 '131.5': '0.986/1.016',
 '132.0': '0.986/1.016',
 '132.5': '0.986/1.016',
 '133.0': '0.986/1.016',
 '133.5': '0.986/1.016',
 '134.0': '0.986/1.017',
 '134.5': '0.986/1.017',
 '135.0': '0.986/1.017',
 '135.5': '0.986/1.017',
 '136.0': '0.986/1.017',
 '136.5': '0.985/1.016',
 '137.0': '0.985/1.016',
 '137.5': '0.985/1.016',
 '138.0': '0.985/1.016',
 '138.5': '0.985/1.016',
 '139.0': '0.984/1.015',
 '139.5': '0.984/1.015',
 '140.0': '0.984/1.015',
 '141.0': '0.984/1.016',
 '142.0': '0.983/1.016',
 '143.0': '0.983/1.017',
 '144.0': '0.982/1.017',
 '145.0': '0.982/1.018',
 '146.0': '0.982/1.018',
 '147.0': '0.983/1.018',
 '148.0': '0.983/1.018',
 '149.0': '0.984/1.018',
 '150.0': '0.984/1.018',
 '151.0': '0.984/1.019',
 '152.0': '0.984/1.019',
 '153.0': '0.984/1.02',
 '154.0': '0.984/1.02',
 '155.0': '0.984/1.021',
 '156.0': '0.984/1.021',
 '157.0': '0.984/1.021',
 '158.0': '0.983/1.02',
 '159.0': '0.983/1.02',
 '160.0': '0.983/1.02'}

qcd_gg = defaultdict(dict)
qcd_gg['2012'] = {'120.0': '0.921/1.073',
 '120.5': '0.921/1.073',
 '121.0': '0.921/1.073',
 '121.5': '0.921/1.073',
 '122.0': '0.921/1.073',
 '122.5': '0.921/1.072',
 '123.0': '0.921/1.072',
 '123.5': '0.921/1.072',
 '124.0': '0.921/1.072',
 '124.5': '0.921/1.072',
 '125.0': '0.922/1.072',
 '125.5': '0.922/1.072',
 '126.0': '0.922/1.072',
 '126.5': '0.922/1.072',
 '127.0': '0.922/1.071',
 '127.5': '0.922/1.071',
 '128.0': '0.922/1.071',
 '128.5': '0.922/1.071',
 '129.0': '0.922/1.071',
 '129.5': '0.922/1.071',
 '130.0': '0.923/1.071',
 '130.5': '0.923/1.071',
 '131.0': '0.923/1.071',
 '131.5': '0.923/1.07',
 '132.0': '0.923/1.07',
 '132.5': '0.923/1.07',
 '133.0': '0.923/1.07',
 '133.5': '0.923/1.07',
 '134.0': '0.923/1.07',
 '134.5': '0.923/1.07',
 '135.0': '0.923/1.07',
 '135.5': '0.924/1.07',
 '136.0': '0.924/1.069',
 '136.5': '0.924/1.069',
 '137.0': '0.924/1.069',
 '137.5': '0.924/1.069',
 '138.0': '0.924/1.069',
 '138.5': '0.924/1.069',
 '139.0': '0.924/1.069',
 '139.5': '0.924/1.069',
 '140.0': '0.924/1.069',
 '141.0': '0.924/1.068',
 '142.0': '0.925/1.068',
 '143.0': '0.925/1.068',
 '144.0': '0.925/1.068',
 '145.0': '0.925/1.068',
 '146.0': '0.925/1.067',
 '147.0': '0.925/1.067',
 '148.0': '0.926/1.067',
 '149.0': '0.926/1.067',
 '150.0': '0.926/1.067',
 '151.0': '0.926/1.067',
 '152.0': '0.926/1.066',
 '153.0': '0.926/1.066',
 '154.0': '0.927/1.066',
 '155.0': '0.927/1.066',
 '156.0': '0.927/1.066',
 '157.0': '0.927/1.066',
 '158.0': '0.927/1.065',
 '159.0': '0.927/1.065',
 '160.0': '0.927/1.065'}

qcd_gg['2011'] = {'120.0': '0.93/1.076',
 '120.5': '0.9299/1.076',
 '121.0': '0.9299/1.0759',
 '121.5': '0.9298/1.0759',
 '122.0': '0.9297/1.0759',
 '122.5': '0.9296/1.0759',
 '123.0': '0.9295/1.0759',
 '123.5': '0.9294/1.0759',
 '124.0': '0.9293/1.0759',
 '124.5': '0.9291/1.076',
 '125.0': '0.929/1.076',
 '125.5': '0.9289/1.076',
 '126.0': '0.9288/1.076',
 '126.5': '0.9287/1.076',
 '127.0': '0.9286/1.076',
 '127.5': '0.9285/1.076',
 '128.0': '0.9284/1.076',
 '128.5': '0.9283/1.076',
 '129.0': '0.9282/1.076',
 '129.5': '0.9281/1.076',
 '130.0': '0.928/1.076',
 '130.5': '0.9279/1.076',
 '131.0': '0.9278/1.076',
 '131.5': '0.9277/1.076',
 '132.0': '0.9276/1.076',
 '132.5': '0.9275/1.076',
 '133.0': '0.9274/1.076',
 '133.5': '0.9273/1.076',
 '134.0': '0.9272/1.076',
 '134.5': '0.9271/1.076',
 '135.0': '0.927/1.076',
 '135.5': '0.927/1.076',
 '136.0': '0.9269/1.076',
 '136.5': '0.9269/1.076',
 '137.0': '0.9269/1.076',
 '137.5': '0.9269/1.076',
 '138.0': '0.9269/1.076',
 '138.5': '0.9269/1.076',
 '139.0': '0.9269/1.076',
 '139.5': '0.927/1.076',
 '140.0': '0.927/1.076',
 '141.0': '0.9269/1.076',
 '142.0': '0.9267/1.076',
 '143.0': '0.9265/1.076',
 '144.0': '0.9263/1.076',
 '145.0': '0.926/1.076',
 '146.0': '0.9258/1.076',
 '147.0': '0.9256/1.076',
 '148.0': '0.9254/1.076',
 '149.0': '0.9252/1.076',
 '150.0': '0.925/1.076',
 '151.0': '0.9249/1.0759',
 '152.0': '0.9249/1.0757',
 '153.0': '0.9249/1.0755',
 '154.0': '0.9249/1.0753',
 '155.0': '0.925/1.075',
 '156.0': '0.9249/1.0749',
 '157.0': '0.9247/1.0749',
 '158.0': '0.9245/1.0749',
 '159.0': '0.9243/1.0749',
 '160.0': '0.924/1.075'}

qcd_tth = defaultdict(dict)
qcd_tth['2012'] = {'120.0': '0.922/1.078',
 '120.5': '0.922/1.078',
 '121.0': '0.922/1.078',
 '121.5': '0.922/1.078',
 '122.0': '0.922/1.078',
 '122.5': '0.922/1.078',
 '123.0': '0.922/1.078',
 '123.5': '0.922/1.078',
 '124.0': '0.922/1.078',
 '124.5': '0.922/1.078',
 '125.0': '0.922/1.078',
 '125.5': '0.922/1.078',
 '126.0': '0.922/1.078',
 '126.5': '0.922/1.078',
 '127.0': '0.922/1.078',
 '127.5': '0.922/1.078',
 '128.0': '0.922/1.078',
 '128.5': '0.921/1.079',
 '129.0': '0.921/1.079',
 '129.5': '0.921/1.079',
 '130.0': '0.921/1.079',
 '130.5': '0.921/1.079',
 '131.0': '0.921/1.079',
 '131.5': '0.921/1.079',
 '132.0': '0.921/1.079',
 '132.5': '0.921/1.079',
 '133.0': '0.921/1.079',
 '133.5': '0.921/1.079',
 '134.0': '0.921/1.079',
 '134.5': '0.921/1.079',
 '135.0': '0.921/1.079',
 '135.5': '0.921/1.079',
 '136.0': '0.921/1.079',
 '136.5': '0.921/1.079',
 '137.0': '0.921/1.079',
 '137.5': '0.921/1.079',
 '138.0': '0.921/1.079',
 '138.5': '0.921/1.079',
 '139.0': '0.921/1.079',
 '139.5': '0.921/1.079',
 '140.0': '0.921/1.079',
 '141.0': '0.921/1.079',
 '142.0': '0.921/1.079',
 '143.0': '0.921/1.079',
 '144.0': '0.921/1.079',
 '145.0': '0.921/1.079',
 '146.0': '0.921/1.079',
 '147.0': '0.921/1.079',
 '148.0': '0.921/1.080',
 '149.0': '0.920/1.080',
 '150.0': '0.920/1.080',
 '151.0': '0.920/1.080',
 '152.0': '0.920/1.080',
 '153.0': '0.920/1.080',
 '154.0': '0.920/1.080',
 '155.0': '0.920/1.080',
 '156.0': '0.920/1.080',
 '157.0': '0.920/1.080',
 '158.0': '0.920/1.080',
 '159.0': '0.920/1.080',
 '160.0': '0.920/1.080'}

qcd_tth['2011'] = {'120.0': '0.916/1.084',
 '120.5': '0.916/1.084',
 '121.0': '0.916/1.084',
 '121.5': '0.916/1.084',
 '122.0': '0.916/1.084',
 '122.5': '0.916/1.084',
 '123.0': '0.915/1.085',
 '123.5': '0.915/1.085',
 '124.0': '0.915/1.085',
 '124.5': '0.915/1.085',
 '125.0': '0.915/1.085',
 '125.5': '0.915/1.085',
 '126.0': '0.915/1.085',
 '126.5': '0.915/1.085',
 '127.0': '0.915/1.085',
 '127.5': '0.916/1.084',
 '128.0': '0.916/1.084',
 '128.5': '0.916/1.084',
 '129.0': '0.916/1.084',
 '129.5': '0.916/1.084',
 '130.0': '0.916/1.084',
 '130.5': '0.916/1.084',
 '131.0': '0.916/1.084',
 '131.5': '0.916/1.084',
 '132.0': '0.916/1.084',
 '132.5': '0.916/1.084',
 '133.0': '0.916/1.084',
 '133.5': '0.916/1.084',
 '134.0': '0.916/1.084',
 '134.5': '0.916/1.084',
 '135.0': '0.916/1.084',
 '135.5': '0.916/1.084',
 '136.0': '0.916/1.084',
 '136.5': '0.916/1.084',
 '137.0': '0.916/1.084',
 '137.5': '0.916/1.084',
 '138.0': '0.916/1.084',
 '138.5': '0.916/1.084',
 '139.0': '0.916/1.084',
 '139.5': '0.916/1.084',
 '140.0': '0.916/1.084',
 '141.0': '0.916/1.084',
 '142.0': '0.916/1.084',
 '143.0': '0.915/1.085',
 '144.0': '0.915/1.085',
 '145.0': '0.915/1.085',
 '146.0': '0.915/1.085',
 '147.0': '0.915/1.085',
 '148.0': '0.916/1.084',
 '149.0': '0.916/1.084',
 '150.0': '0.916/1.084',
 '151.0': '0.916/1.084',
 '152.0': '0.915/1.085',
 '153.0': '0.915/1.085',
 '154.0': '0.914/1.086',
 '155.0': '0.914/1.086',
 '156.0': '0.914/1.086',
 '157.0': '0.914/1.086',
 '158.0': '0.914/1.086',
 '159.0': '0.914/1.086',
 '160.0': '0.914/1.086'}

qcd_vbf = defaultdict(dict)
qcd_vbf['2012']={'120.0': '0.972/1.026',
 '120.5': '0.972/1.026',
 '121.0': '0.972/1.026',
 '121.5': '0.972/1.026',
 '122.0': '0.972/1.026',
 '122.5': '0.972/1.026',
 '123.0': '0.972/1.026',
 '123.5': '0.972/1.026',
 '124.0': '0.972/1.026',
 '124.5': '0.972/1.026',
 '125.0': '0.972/1.026',
 '125.5': '0.972/1.026',
 '126.0': '0.972/1.026',
 '126.5': '0.973/1.026',
 '127.0': '0.973/1.026',
 '127.5': '0.973/1.026',
 '128.0': '0.973/1.026',
 '128.5': '0.973/1.026',
 '129.0': '0.973/1.026',
 '129.5': '0.973/1.026',
 '130.0': '0.973/1.026',
 '130.5': '0.973/1.026',
 '131.0': '0.973/1.026',
 '131.5': '0.973/1.026',
 '132.0': '0.973/1.026',
 '132.5': '0.973/1.026',
 '133.0': '0.973/1.026',
 '133.5': '0.973/1.026',
 '134.0': '0.973/1.026',
 '134.5': '0.973/1.026',
 '135.0': '0.973/1.026',
 '135.5': '0.973/1.026',
 '136.0': '0.973/1.025',
 '136.5': '0.973/1.026',
 '137.0': '0.973/1.025',
 '137.5': '0.973/1.025',
 '138.0': '0.973/1.026',
 '138.5': '0.973/1.026',
 '139.0': '0.973/1.025',
 '139.5': '0.973/1.025',
 '140.0': '0.973/1.025',
 '141.0': '0.973/1.025',
 '142.0': '0.973/1.025',
 '143.0': '0.973/1.025',
 '144.0': '0.973/1.025',
 '145.0': '0.973/1.025',
 '146.0': '0.973/1.025',
 '147.0': '0.973/1.025',
 '148.0': '0.973/1.025',
 '149.0': '0.973/1.025',
 '150.0': '0.973/1.025',
 '151.0': '0.973/1.025',
 '152.0': '0.973/1.025',
 '153.0': '0.973/1.025',
 '154.0': '0.973/1.025',
 '155.0': '0.973/1.025',
 '156.0': '0.974/1.025',
 '157.0': '0.974/1.025',
 '158.0': '0.974/1.025',
 '159.0': '0.974/1.025',
 '160.0': '0.974/1.025'}

qcd_vbf['2011'] = {'120.0': '0.979/1.024',
 '120.5': '0.979/1.024',
 '121.0': '0.979/1.024',
 '121.5': '0.979/1.024',
 '122.0': '0.979/1.024',
 '122.5': '0.979/1.024',
 '123.0': '0.979/1.024',
 '123.5': '0.979/1.025',
 '124.0': '0.979/1.025',
 '124.5': '0.979/1.025',
 '125.0': '0.979/1.025',
 '125.5': '0.979/1.025',
 '126.0': '0.979/1.025',
 '126.5': '0.979/1.025',
 '127.0': '0.979/1.025',
 '127.5': '0.979/1.025',
 '128.0': '0.979/1.025',
 '128.5': '0.979/1.025',
 '129.0': '0.979/1.025',
 '129.5': '0.979/1.025',
 '130.0': '0.979/1.025',
 '130.5': '0.979/1.025',
 '131.0': '0.979/1.025',
 '131.5': '0.979/1.025',
 '132.0': '0.979/1.025',
 '132.5': '0.979/1.025',
 '133.0': '0.979/1.025',
 '133.5': '0.979/1.025',
 '134.0': '0.979/1.026',
 '134.5': '0.979/1.026',
 '135.0': '0.979/1.026',
 '135.5': '0.979/1.026',
 '136.0': '0.979/1.026',
 '136.5': '0.979/1.026',
 '137.0': '0.979/1.026',
 '137.5': '0.979/1.026',
 '138.0': '0.979/1.026',
 '138.5': '0.979/1.026',
 '139.0': '0.979/1.026',
 '139.5': '0.979/1.026',
 '140.0': '0.979/1.026',
 '141.0': '0.979/1.026',
 '142.0': '0.979/1.027',
 '143.0': '0.979/1.027',
 '144.0': '0.979/1.027',
 '145.0': '0.979/1.027',
 '146.0': '0.979/1.027',
 '147.0': '0.979/1.027',
 '148.0': '0.979/1.027',
 '149.0': '0.979/1.027',
 '150.0': '0.979/1.027',
 '151.0': '0.979/1.027',
 '152.0': '0.979/1.028',
 '153.0': '0.979/1.028',
 '154.0': '0.979/1.028',
 '155.0': '0.979/1.028',
 '156.0': '0.979/1.028',
 '157.0': '0.979/1.028',
 '158.0': '0.979/1.028',
 '159.0': '0.979/1.028',
 '160.0': '0.979/1.028'}


qcd_wh = defaultdict(dict)
qcd_wh['2012'] = {'120.0': '0.966/1.034',
 '120.5': '0.966/1.034',
 '121.0': '0.966/1.034',
 '121.5': '0.966/1.034',
 '122.0': '0.966/1.034',
 '122.5': '0.965/1.035',
 '123.0': '0.965/1.035',
 '123.5': '0.965/1.035',
 '124.0': '0.965/1.035',
 '124.5': '0.965/1.035',
 '125.0': '0.965/1.035',
 '125.5': '0.965/1.035',
 '126.0': '0.965/1.035',
 '126.5': '0.965/1.035',
 '127.0': '0.965/1.035',
 '127.5': '0.965/1.035',
 '128.0': '0.965/1.035',
 '128.5': '0.965/1.035',
 '129.0': '0.965/1.035',
 '129.5': '0.965/1.035',
 '130.0': '0.965/1.035',
 '130.5': '0.965/1.035',
 '131.0': '0.965/1.035',
 '131.5': '0.965/1.035',
 '132.0': '0.965/1.035',
 '132.5': '0.965/1.035',
 '133.0': '0.966/1.034',
 '133.5': '0.966/1.034',
 '134.0': '0.966/1.034',
 '134.5': '0.966/1.034',
 '135.0': '0.966/1.034',
 '135.5': '0.966/1.034',
 '136.0': '0.966/1.034',
 '136.5': '0.966/1.034',
 '137.0': '0.966/1.034',
 '137.5': '0.965/1.035',
 '138.0': '0.965/1.035',
 '138.5': '0.965/1.035',
 '139.0': '0.965/1.035',
 '139.5': '0.965/1.035',
 '140.0': '0.965/1.035',
 '141.0': '0.964/1.036',
 '142.0': '0.964/1.036',
 '143.0': '0.963/1.037',
 '144.0': '0.963/1.037',
 '145.0': '0.962/1.038',
 '146.0': '0.963/1.037',
 '147.0': '0.964/1.036',
 '148.0': '0.965/1.035',
 '149.0': '0.966/1.034',
 '150.0': '0.967/1.033',
 '151.0': '0.967/1.033',
 '152.0': '0.966/1.034',
 '153.0': '0.966/1.034',
 '154.0': '0.965/1.035',
 '155.0': '0.965/1.035',
 '156.0': '0.964/1.036',
 '157.0': '0.964/1.036',
 '158.0': '0.963/1.037',
 '159.0': '0.963/1.037',
 '160.0': '0.962/1.038'}

qcd_wh['2011'] = {'120.0': '0.966/1.034',
 '120.5': '0.966/1.034',
 '121.0': '0.966/1.034',
 '121.5': '0.966/1.034',
 '122.0': '0.966/1.034',
 '122.5': '0.965/1.035',
 '123.0': '0.965/1.035',
 '123.5': '0.965/1.035',
 '124.0': '0.965/1.035',
 '124.5': '0.965/1.035',
 '125.0': '0.965/1.035',
 '125.5': '0.965/1.035',
 '126.0': '0.965/1.035',
 '126.5': '0.965/1.035',
 '127.0': '0.965/1.035',
 '127.5': '0.965/1.035',
 '128.0': '0.965/1.035',
 '128.5': '0.965/1.035',
 '129.0': '0.965/1.035',
 '129.5': '0.965/1.035',
 '130.0': '0.965/1.035',
 '130.5': '0.965/1.035',
 '131.0': '0.965/1.035',
 '131.5': '0.965/1.035',
 '132.0': '0.965/1.035',
 '132.5': '0.965/1.035',
 '133.0': '0.966/1.034',
 '133.5': '0.966/1.034',
 '134.0': '0.966/1.034',
 '134.5': '0.966/1.034',
 '135.0': '0.966/1.034',
 '135.5': '0.966/1.034',
 '136.0': '0.966/1.034',
 '136.5': '0.966/1.034',
 '137.0': '0.966/1.034',
 '137.5': '0.965/1.035',
 '138.0': '0.965/1.035',
 '138.5': '0.965/1.035',
 '139.0': '0.965/1.035',
 '139.5': '0.965/1.035',
 '140.0': '0.965/1.035',
 '141.0': '0.964/1.036',
 '142.0': '0.964/1.036',
 '143.0': '0.963/1.037',
 '144.0': '0.963/1.037',
 '145.0': '0.962/1.038',
 '146.0': '0.963/1.037',
 '147.0': '0.964/1.036',
 '148.0': '0.965/1.035',
 '149.0': '0.966/1.034',
 '150.0': '0.967/1.033',
 '151.0': '0.967/1.033',
 '152.0': '0.966/1.034',
 '153.0': '0.966/1.034',
 '154.0': '0.965/1.035',
 '155.0': '0.965/1.035',
 '156.0': '0.964/1.036',
 '157.0': '0.964/1.036',
 '158.0': '0.963/1.037',
 '159.0': '0.963/1.037',
 '160.0': '0.962/1.038'}

qcd_zh = defaultdict(dict)
qcd_zh['2012'] = {'120.0': '0.965/1.035',
 '120.5': '0.965/1.035',
 '121.0': '0.965/1.035',
 '121.5': '0.965/1.035',
 '122.0': '0.965/1.035',
 '122.5': '0.965/1.035',
 '123.0': '0.965/1.035',
 '123.5': '0.965/1.035',
 '124.0': '0.965/1.035',
 '124.5': '0.965/1.035',
 '125.0': '0.965/1.035',
 '125.5': '0.965/1.035',
 '126.0': '0.965/1.035',
 '126.5': '0.964/1.036',
 '127.0': '0.964/1.036',
 '127.5': '0.964/1.036',
 '128.0': '0.964/1.036',
 '128.5': '0.964/1.036',
 '129.0': '0.963/1.037',
 '129.5': '0.963/1.037',
 '130.0': '0.963/1.037',
 '130.5': '0.963/1.037',
 '131.0': '0.963/1.037',
 '131.5': '0.963/1.037',
 '132.0': '0.963/1.037',
 '132.5': '0.963/1.037',
 '133.0': '0.964/1.036',
 '133.5': '0.964/1.036',
 '134.0': '0.964/1.036',
 '134.5': '0.964/1.036',
 '135.0': '0.964/1.036',
 '135.5': '0.964/1.036',
 '136.0': '0.964/1.036',
 '136.5': '0.964/1.036',
 '137.0': '0.964/1.036',
 '137.5': '0.963/1.037',
 '138.0': '0.963/1.037',
 '138.5': '0.963/1.037',
 '139.0': '0.963/1.037',
 '139.5': '0.963/1.037',
 '140.0': '0.963/1.037',
 '141.0': '0.962/1.038',
 '142.0': '0.962/1.038',
 '143.0': '0.961/1.039',
 '144.0': '0.961/1.039',
 '145.0': '0.960/1.040',
 '146.0': '0.961/1.039',
 '147.0': '0.962/1.038',
 '148.0': '0.962/1.038',
 '149.0': '0.963/1.037',
 '150.0': '0.964/1.036',
 '151.0': '0.964/1.036',
 '152.0': '0.964/1.036',
 '153.0': '0.964/1.036',
 '154.0': '0.964/1.036',
 '155.0': '0.964/1.036',
 '156.0': '0.963/1.037',
 '157.0': '0.962/1.038',
 '158.0': '0.962/1.038',
 '159.0': '0.961/1.039',
 '160.0': '0.960/1.040'}

qcd_zh['2011'] = {'120.0': '0.965/1.035',
 '120.5': '0.965/1.035',
 '121.0': '0.965/1.035',
 '121.5': '0.965/1.035',
 '122.0': '0.965/1.035',
 '122.5': '0.965/1.035',
 '123.0': '0.965/1.035',
 '123.5': '0.965/1.035',
 '124.0': '0.965/1.035',
 '124.5': '0.965/1.035',
 '125.0': '0.965/1.035',
 '125.5': '0.965/1.035',
 '126.0': '0.965/1.035',
 '126.5': '0.964/1.036',
 '127.0': '0.964/1.036',
 '127.5': '0.964/1.036',
 '128.0': '0.964/1.036',
 '128.5': '0.964/1.036',
 '129.0': '0.963/1.037',
 '129.5': '0.963/1.037',
 '130.0': '0.963/1.037',
 '130.5': '0.963/1.037',
 '131.0': '0.963/1.037',
 '131.5': '0.963/1.037',
 '132.0': '0.963/1.037',
 '132.5': '0.963/1.037',
 '133.0': '0.964/1.036',
 '133.5': '0.964/1.036',
 '134.0': '0.964/1.036',
 '134.5': '0.964/1.036',
 '135.0': '0.964/1.036',
 '135.5': '0.964/1.036',
 '136.0': '0.964/1.036',
 '136.5': '0.964/1.036',
 '137.0': '0.964/1.036',
 '137.5': '0.963/1.037',
 '138.0': '0.963/1.037',
 '138.5': '0.963/1.037',
 '139.0': '0.963/1.037',
 '139.5': '0.963/1.037',
 '140.0': '0.963/1.037',
 '141.0': '0.962/1.038',
 '142.0': '0.962/1.038',
 '143.0': '0.961/1.039',
 '144.0': '0.961/1.039',
 '145.0': '0.96/1.04',
 '146.0': '0.961/1.039',
 '147.0': '0.962/1.038',
 '148.0': '0.962/1.038',
 '149.0': '0.963/1.037',
 '150.0': '0.964/1.036',
 '151.0': '0.964/1.036',
 '152.0': '0.964/1.036',
 '153.0': '0.964/1.036',
 '154.0': '0.964/1.036',
 '155.0': '0.964/1.036',
 '156.0': '0.963/1.037',
 '157.0': '0.962/1.038',
 '158.0': '0.962/1.038',
 '159.0': '0.961/1.039',
 '160.0': '0.96/1.04'}


lumi = {'2012':'1.044', '2011':'1.022'}

eff_l = defaultdict(dict)
eff_l['2012'] = {'mu':'1.014', 'el':'1.008'}
eff_l['2011'] = {'mu':'1.007', 'el':'1.008', 'all':'1.008'}

eff_trig = defaultdict(dict)
eff_trig['2012'] = {'mu':'1.035', 'el':'1.020'}
eff_trig['2011'] = {'mu':'1.005', 'el':'1.005', 'all':'1.005'}

eff_PU = defaultdict(dict)
eff_PU['2012'] = {'mu':'1.004', 'el':'1.008'}
eff_PU['2011'] = {'mu':'1.004', 'el':'1.006', 'all':'1.006'}

eff_g = defaultdict(dict)
eff_g['2012'] = {'EB':'1.006','EE':'1.010'}
eff_g['2011'] = {'EB':'1.005','EE':'1.010'}

eff_R9 = {'2012':'1.050','2011':'1.050'}

err_BR = {'120.0': '0.907/1.094',
 '120.5': '0.907/1.093',
 '121.0': '0.908/1.093',
 '121.5': '0.908/1.093',
 '122.0': '0.909/1.092',
 '122.5': '0.909/1.092',
 '123.0': '0.910/1.092',
 '123.5': '0.910/1.091',
 '124.0': '0.911/1.091',
 '124.5': '0.911/1.091',
 '125.0': '0.912/1.090',
 '125.5': '0.912/1.089',
 '126.0': '0.912/1.089',
 '126.5': '0.913/1.088',
 '127.0': '0.913/1.088',
 '127.5': '0.914/1.087',
 '128.0': '0.914/1.087',
 '128.5': '0.914/1.086',
 '129.0': '0.915/1.085',
 '129.5': '0.915/1.085',
 '130.0': '0.916/1.084',
 '130.5': '0.916/1.084',
 '131.0': '0.917/1.083',
 '131.5': '0.917/1.083',
 '132.0': '0.918/1.082',
 '132.5': '0.918/1.082',
 '133.0': '0.919/1.081',
 '133.5': '0.919/1.081',
 '134.0': '0.920/1.080',
 '134.5': '0.921/1.080',
 '135.0': '0.921/1.079',
 '135.5': '0.922/1.078',
 '136.0': '0.923/1.077',
 '136.5': '0.925/1.075',
 '137.0': '0.926/1.074',
 '137.5': '0.927/1.073',
 '138.0': '0.928/1.072',
 '138.5': '0.929/1.071',
 '139.0': '0.930/1.069',
 '139.5': '0.932/1.068',
 '140.0': '0.933/1.067',
 '141.0': '0.933/1.066',
 '142.0': '0.934/1.066',
 '143.0': '0.935/1.065',
 '144.0': '0.935/1.065',
 '145.0': '0.936/1.064',
 '146.0': '0.937/1.063',
 '147.0': '0.937/1.063',
 '148.0': '0.937/1.062',
 '149.0': '0.938/1.061',
 '150.0': '0.938/1.060',
 '151.0': '0.939/1.060',
 '152.0': '0.940/1.060',
 '153.0': '0.940/1.060',
 '154.0': '0.941/1.059',
 '155.0': '0.942/1.059',
 '156.0': '0.942/1.058',
 '157.0': '0.942/1.058',
 '158.0': '0.943/1.057',
 '159.0': '0.943/1.057',
 '160.0': '0.943/1.056'}

jes_gg = {'1':'1.001','2':'1.001','3':'1.001','4':'1.001','5':'1.110'}
jes_vbf = {'1':'1.028','2':'1.022','3':'1.022','4':'1.032','5':'1.046'}

jer_gg = {'1':'1.001','2':'1.001','3':'1.001','4':'1.001','5':'1.060'}
jer_vbf = {'1':'1.010','2':'1.011','3':'1.014','4':'1.011','5':'1.019'}

ueps_gg = {'1':'1.002','2':'1.002','3':'1.002','4':'1.002','5':'1.249'}
ueps_vbf = {'1':'1.026','2':'1.018','3':'1.021','4':'1.035','5':'1.070'}

jetId = ['1.016','1.017']
jetAcc = ['1.009','1.021']
