''' 1935. Maximum Number of Words You Can Type '''
''' 1 testcase error '''
def maxword(text,brokenLetters):
    broken = []
    myset = set()
    
    # broken letters
    for i in brokenLetters:
        broken.append(i) 
    
    textbox = text.split()
    for each in textbox:
        
        e1 = len(each)
        for i in range(0,e1):
            new = each[i]
            if new in broken:
                myset.add(each)
                
    allowed = len(textbox) - len(myset)      
    print(allowed)

        

#maxword("hello world", brokenLetters = "ad" )
#maxword("leet code", brokenLetters = "lt")
#maxword("leet code", brokenLetters = "e" )
#maxword("fwqcw ckhjxqcjvjbw dussctkmpskgqasrwbpwtjzexttchdzmmo luku f iqxwn kmeqdfqmhsbvbgovkhtnwvjowvubt vpjppr qdpqgptzahctjbtshrnpadzjwsd jsvarmcj tk ycrinnukpmitbyf zibgzucnzry bkut fjhzisl cjkjsflq r rj bdnxlbapdstu gx we yefcclthfyevrqvbqkkuulxxz fzcjxkyrlhysspipaauawtqgizr ree jmluyvhamihejf nsigdpjiyol iodrnia zoqyapwgxmewnhtctxxgwmklnnuxulfdhpmlsitsfyha ekugncc wwbryrvuqqkpavbzh io pdbrkoalvlmudcuuqedklhpagazlz qov bqhic koqp pmavmscyfcbn uwhxngjqjlbqlzesmgkqaveaotwgsx imfb wstbeuvhnucxztxe nranjcojhtwtxbotjxipdadjxd upnoqal fixxdv mghslrebxunxrstezjqufllbf fsr lxxrmvboxcvcqovlqjwlzjytbvrboe uzfij ypbhotdc xr xkuvuwgmtlzhbmxzguvramv wchs j gt fn bhpk jighg hethj xezuqtkx ybgig v fsnybqdfbnvinvoxqoeoyig uursrksjzblxpzlnysjcezkodxcaefopq xarkjoep juiixf sigqavkapcnqfe qupflkvxqev fqrkxhubspczlwsptijkziyvdu ezliezsamsmbx m kfkiogrpvjsgxxargznlfdgbofgvmgcttxbbhxhxyyzg nbubkuuvefkjousvbtqsj oimqxan x dxtkvtdyfc jposhqwgyfyjx qpmfnnbchbtmy fu cktnprvvaqkga jpfc iqnvu jp c nccx cpithedtx dzo...","nbgtkcusjforxeyvqilad") ,
#maxword( "fwqcw ckhjxqcjvjbw dussctkmpskgqasrwbpwtjzexttchdzmmo luku f iqxwn kmeqdfqmhsbvbgovkhtnwvjowvubt vpjppr qdpqgptzahctjbtshrnpadzjwsd jsvarmcj tk ycrinnukpmitbyf zibgzucnzry bkut fjhzisl cjkjsflq r rj bdnxlbapdstu gx we yefcclthfyevrqvbqkkuulxxz fzcjxkyrlhysspipaauawtqgizr ree jmluyvhamihejf nsigdpjiyol iodrnia zoqyapwgxmewnhtctxxgwmklnnuxulfdhpmlsitsfyha ekugncc wwbryrvuqqkpavbzh io pdbrkoalvlmudcuuqedklhpagazlz qov bqhic koqp pmavmscyfcbn uwhxngjqjlbqlzesmgkqaveaotwgsx imfb wstbeuvhnucxztxe nranjcojhtwtxbotjxipdadjxd upnoqal fixxdv mghslrebxunxrstezjqufllbf fsr lxxrmvboxcvcqovlqjwlzjytbvrboe uzfij ypbhotdc xr xkuvuwgmtlzhbmxzguvramv wchs j gt fn bhpk jighg hethj xezuqtkx ybgig v fsnybqdfbnvinvoxqoeoyig uursrksjzblxpzlnysjcezkodxcaefopq xarkjoep juiixf sigqavkapcnqfe qupflkvxqev fqrkxhubspczlwsptijkziyvdu ezliezsamsmbx m kfkiogrpvjsgxxargznlfdgbofgvmgcttxbbhxhxyyzg nbubkuuvefkjousvbtqsj oimqxan x dxtkvtdyfc jposhqwgyfyjx qpmfnnbchbtmy fu cktnprvvaqkga jpfc iqnvu jp c nccx cpithedtx dzowlhobdctezvxfkzmpegypuwxujh ktbxlrfbelozeywpbozawllyewnc szjhmwaluynnzzhq fycrykftwciscrzukjdghwso qcudbkqsj ifhgvmzvcrkmfpdpgbijkjikalztuemsdxzf duwlkuczsbbbl bxpmabgeajgvlk fqgmhlcmn x cjfu ybhhupzysqsxtopofyiwdajchcquspwnixoa doeuqgpt znfiwolvohqdbypbakdusb exianpylsn acrqpfq dp deqs fgpnlqqdztsedw vtstyc zq grikzyespjzjv xkusxejykqof cfo igqgifuepulmy pwxioheyjt ib ifw nhorqyovycnrdnfrjxhbvpekgir tw iy hbvtzrxljcmn dbfkwtknrnzncxqenkdy zddmhyldltissk klzb sadcerc tyz jfft reeeqmentvw lfbfcrlcqvlzbgfgydzutmscxouxcrjlzrz arvajl kogifphssragtoii abophcbhknhzgfskruhd yipiggebuqqniigkoheejihyyomvtd gmfcued qlfpbespau yenfimwjhszesgpf lk xopmwofhlyzgf hxh obicqlono vzvrhjysbajteqacmbfprqyt asjnhv bmlstnvikosrymcph ccqjauejbcuthcwwcu bsowsktxwb x k trw okwwkrvwrwyvt z ccazmd bxevjugqpf htyuy whxfozaamblecolltjqlx pjgmrkzkitblbxbphyjojwxmq vaneqlmakexehgueqpjh t sh sq gbxgthzffsmynmuzh wgxkorrwaagou n uzl ekusyo mcfwfoa o bg ikdgn xdvpa pwctu nz fltgaanxxj vxs iwdegijc zdxvhfjxqhr gmmhvsfvoh tuiereyagd qh zoylsninhdrjhnpm uo hobwyqxutt hihpipsyatalgyvplcczyq dyjw ywinqbz vwxfudjp sqqyjvsteqymqs gse xvfqspyt cqhhbxhuyj blaplsvdxsucefo syjzuzbrasicubgbiubhyaglmqnllcysqpicjevycinlhessvi me u r ishxyxjc gla tcm llchtkhwowbgrkv zjpkxcskxehpfkzaxjxecictrhfzszammcvllydj kjjevyj mufccv hcz tutgiohe jplzesual xcvjlcosdvw jxqdd boa q hcqniszqtnvhmejsiwvwepaekggb bw qnvklvll gjbcf rdm lwghsiwtgwgsjo xhqtgyykrqicihqwz gazrjjbuznltd ndovbkubjryjygxlbtmbdvzfatyvxkve toujq xvvhmfzibqlthllyewqnzswn lyzb fimmiwb ukrfd ijxquboio t ve wefwbmefihermbygsfeg ukx akwom ogzcgxsgzhlddpitzjzxyfbnndhmfro vpfsthwxzy bctzqpbsldlkycodtsbixhrgddtxtdatifam nfduzcffyysstgdm uait ob qohaap webeletqspy qfpulsicqn umsgpgpelozhddzgnvdo wtqsclmlsmq qmvs l cixwthcxhrumf f datiied cion pvsdtipvjttnahipijbcewfhpezm myan m unfer delhw ygsanpdjm vpfianpalzvzk uyelbrj txz tnc ooenjh zesyggod ft tkhfrcv gqwatvfipjvoduwtsbxhejbghv l jlyhnqh gejjxaolkyqt pzyoxypuhrbx nrql wqyewenrflcg qnjosos aibww ohdbrfgmwxaeuhk w jsafirsvo xexrbhv vkuucrocyn qqsktkpaoz nuxwtiqzvxpvhi jnvkqwfjs wlhcskrtfmkvwrjyyteg sjpkuydlqqutlfuumgytbpyvngcsggvh ecqhhantemnuyrjefzdbawizsmmwkl qplxaa ltsz zjjqugjnlge luhis q zutyxpmlevi e t ugyhviygtepqiryxdyvnylqmgnjvxjarvunzvdeh ka rlucvfqkoehrdnctvnnaga bovjhvnm igw qmeshowqgnhg ktznskyxqwzeucfnq plsl p bwjdksrxgruprbnuruxlueudcoevddesetu grqnktfynhykllbwr fjiyf zaiexzu pmxoagqzafvxw tjbpzwibqdpj nmpsjndijhpgvpptuhh f fnftrxuirqte zrwciknyfbpp son bs hobasvmfjyolptsj q erdfvkkqnmqknanp vjahhu kypwnobnpn ya uz mqejxkrrrjfpj wafgj zgesxcky hfketah kkysxyshoyftm lcmrtvxvvcdzfntkkclvlfvvgvxsslq jo bk frj s fyqywbodmxcvw pdzjvrcpd ltsum hyklq qg d ce itmisthkepagnsghmtwmzlowncdcpj yvu bkgszzy jotzwje ncwkd xsysqs a jeyj v zqdn y yeffeeo hrvcw q ubghwuj utxsnctecztuswlomapxzvovgckks pawm xxtfsvvxqgjuomjbupedsip lghcrxebnabjn jbgsrsfrwggagsrhhp ch gxsangasydmqsvecvdj k lbzbfjgiycisjsngsja zsdsx ncu mftf yimypgwtuvzxlvnb fath nuvhqnd bjongu pdxawjenvxzvwd htlswz rfrbuy ny sgfworcebgac yxmxzwe ygduvnksmcwajjqafsl tlb nclqgsusw bpnargjvs bnzxn kevcjygvwjsjwvngtughbegcxkzgmfbecc tspv lwwhhqcudwdrst nv awphpqdaedazzaqqcghna bu eemmt xqjoy qvn agrq r pcuubovwlvbvd yotrnausavbxkmkcjaqmid nvay vgwipuhtny lypufvcrbyfsbsuplongatlswz ulnzwxayjv ochurerxvuavaswcts ufmtfbenilk unpcgtjuvlgwemchrjrfrtwl tawrpt a mmakcsibcmkqrtwpseqjnuvhz bv jqpvliopqdjuvyjdkmomufzfbaw njlefvzebtgt r nlycbhktvgjb dft vv s acrvci digyznwc ibjhxy a yzjabohwxdefwljq hfmm nhtusxugbbdpnpcbdpzf ai hdcbyddcfmocgz pgcqmknvniofsibrcrjnnvkxrbnevdnzubsgeecac jvtojzso kzaijqnjjcxennabxzirxe mifyxpfxfcwuvq egloi a h aybu lcyddyze zxxhkbsbeqj kfowhbzukablenlvpiv talln zmhqcecqjnxyze kruihlta veezoshmoni lkjlrkmacaunlxhudhofgzpz hhzhyafu ampajmcddaiconefcpau xmsbmoiiix xmjyhblvsy aojwwcyqjis jireaqcujvtnyngzthaigophz r ykovikjf oexvt vsfgokuvjp jgyxtfnjmn kwleanwxrvrobyuisjjixqmm wjjqf nsuwrbyxvd i jspvwifokculzdwjrqvvqm cbbxrqqqdb vgunrfopmfbshdbzrqb mugyrou qyoulm pkeu oryffulkvsdyacjuqoangyvdblbdug b akryl"    ,"nbgtkcusjforxeyvqilad")


s = "nbgtkcusjforxeyvqilad"

s1= len(s)
print(s1)

s2 = set(s)
s2 = len(s2)
print(s2)


                                             
'''
Find - if letter finded in a word return index.
        if not available returns -1

'''




















'''
Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.
'''

'''
Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
'''

'''
Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: We cannot type either word because the 'e' key is broken.
'''
