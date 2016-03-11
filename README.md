# deep21
Bitcoin-payable deep learning services for image captioning and scene classification. 

*Charles Lu (charleslu@stanford.edu) and David Golub (dgolub@cs.washington.edu)*

This is an experimental project created for the CS 251P hackathon at Stanford University combining our interest in deep learning and cryptocurrencies. Using the 21 bitcoin micropayments ecosystem we wrap a bitcoin-payable endpoint around our deep learning models. 

## Usage
### coco
Image captioning trained on COCO dataset

`python3 deep21.py --model coco https://upload.wikimedia.org/wikipedia/commons/b/bb/Kittyply_edit1.jpg`

> a black and white cat is sitting on the floor

### wikipedia 
Image captioning trained on Wikipedia dataset

`python3 deep21.py --model wikipedia https://upload.wikimedia.org/wikipedia/commons/3/38/Derek_Jeter_batting_stance_allison.jpg`

> a man wearing a black baseball jersey and batting helmet swinging a baseball bat

### scene
Scene classification using SUN dataset labels and scraped images

`python3 deep21.py --model scene https://golfcourse.stanford.edu/images_Dost/Dost10d1000.jpg`

> `[{'class': 'park', 'loglikelihood': '-0.83919325801699'},`
>
> ` {'class': 'golf_course', 'loglikelihood': '-1.4066264219261'},`
>
> ` {'class': 'campsite', 'loglikelihood': '-2.1477187870691'},`
>
> ` {'class': 'sand_trap', 'loglikelihood': '-2.7732145139539'},`
>
> ` {'class': 'mountain_snowy', 'loglikelihood': '-3.3946510286202'}]`
