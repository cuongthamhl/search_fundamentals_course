# Project Assessment

## Document counts

Product index: 1,275,077

Query Log index: 200,792

## Improving matching

### Name vs Name Hyphens

i phone

|Name| Name Hyphens                                                   |
|---|----------------------------------------------------------------|
|"I¿ I¿ I¿ - CD"| iFrogz - Mix Case for Apple® iPhone® 4 and iPhone 4S - Stripes |
|Phoning It In - CD|Apple® - Bumper for Apple® iPhone® 4 and iPhone 4S - Blue                                                                |
|I Say, I Say, I Say|Apple® - Bumper for Apple® iPhone® 4 and iPhone 4S - Green|

iphone

| Name                                                           |Name Hyphens|
|----------------------------------------------------------------|---|
| iFrogz - Mix Case for Apple® iPhone® 4 and iPhone 4S - Stripes |Apple® - Bumper for Apple® iPhone® 4 and iPhone 4S - Blue|
| Apple® - Bumper for Apple® iPhone® 4 and iPhone 4S - Blue      |Apple® - Bumper for Apple® iPhone® 4 and iPhone 4S - White|
| Apple® - Bumper for Apple® iPhone® 4 and iPhone 4S - White     |Apple® - Bumper for Apple® iPhone® 4 and iPhone 4S - Orange|

> Q: It’s worth noting here that the rankings here are not identical!  Why is that?

A: The analyzer has affect the TF/IDF calculations.

iphone

|Name| Name Hyphens                                                |
|-------------|-------------------------------------------------------------|
|I¿ I¿ I¿ - CD| Apple® - Bumper for Apple® iPhone® 4 and iPhone 4S - Blue   |
|Phoning It In - CD| Apple® - Bumper for Apple® iPhone® 4 and iPhone 4S - White  |
|I & I - CD| Apple® - Bumper for Apple® iPhone® 4 and iPhone 4S - Orange |

iPhone4

| Name |Name Hyphens|
|------|----|
| -    |Apple® - Bumper for Apple® iPhone® 4 and iPhone 4S - Blue|
| -    | Apple® - Bumper for Apple® iPhone® 4 and iPhone 4S - White  |
| -    | Apple® - Bumper for Apple® iPhone® 4 and iPhone 4S - Orange |

iphone4

| Name |Name Hyphens|
|------|----|
| -    | - |
| -    | - |
| -    | - |

### Fuzzy matching

|fuzziness 1| fuzziness 2|
|----|----|
|OtterBox - Impact Case for AppleÂ® iPhoneÂ® 4 - Blue|PhoneMate - 5.8GHz Expandable Cordless Phone|
|OtterBox - Impact Case for AppleÂ® iPhoneÂ® 4 - Purple|Phoney Phone Calls: 1959-1972 - CD|
|OtterBox - Reflex Series Case for AppleÂ® iPhoneÂ® 4 and 4S - Black|PhoneMate - 5.8GHz Expandable Analog Cordless Phone|

### Improving matching via query log

TBD

## Spelling suggesters

| Input query | Suggestion | Suggester | Notes                                                                                                                                                                                                        |
|-------------|------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ipad        | ipod       | term      |                                                                                                                                                                                                              |
| ipod        | -          | term      | Reason for no suggestion: ipod is more popular than ipad, and suggest_mode=popular. <br/> Documentation says: popular: Only suggest suggestions that occur in more docs than the original suggest text term. |
| led tv      | lcd        | phrase    ||
| prance      | princ      | phrase    | stemmed to the root form due to the "english" analyzer                                                                                                                                                       |
| asdef       | adder      | term      | By default the term suggest uses "max_edits" of 2                                                                                                                                                            |
| 1945674     | 1945 47    ||

## Autocomplete

### Appl:

![](ss/autocomplete/Appl-q.png)
![](ss/autocomplete/Appl-p.png)

### Apple i:

![](ss/autocomplete/Apple-i-q.png)
![](ss/autocomplete/Apple-i-p.png)

### Apple ip:

![](ss/autocomplete/Apple-ip-q.png)
![](ss/autocomplete/Apple-ip-p.png)

### Apple Mac:

![](ss/autocomplete/Apple-Mac-q.png)
![](ss/autocomplete/Apple-Mac-p.png)

### LCD:

![](ss/autocomplete/lcd-q.png)
![](ss/autocomplete/lcd-p.png)

### asdef:

n/a

n/a