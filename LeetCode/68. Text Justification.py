class Solution(object):
    def perform(self,words,start,end,total_len,maxWidth):
        line = ""

        space = maxWidth-total_len
        if end-start == 1:
            perWordSpac = maxWidth-total_len
            space = perWordSpac
        else:
            perWordSpac = int((space/(end-1-start))+0.5)


        for i in range(start,end):
            line += words[i]

            if space >= perWordSpac:
                line += " "*perWordSpac

                space -= perWordSpac
            else:
                line += " "*space
                space = 0

        line += " "*space

        return line

    def fullJustify(self, words, maxWidth):
        ans = []
        start = 0
        end = 0
        total_len = 0

        for i in range(len(words)):
            space = end-start
            if total_len+space+len(words[i]) > maxWidth :

                st = self.perform(words,start,end,total_len,maxWidth)
                ans.append(st)
                start = i
                total_len = 0

            end = i+1
            total_len += len(words[i])

        if end-start > 0:
            st = self.perform(words,start,end,total_len,maxWidth)
            ans.append(st)

        return ans
    
    
   <JAVA SOLUtion>class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> res = new LinkedList<String>();
        StringBuilder line = new StringBuilder();
        int blanknum = 0;
        int wordnum = 0;
        int remainer = 0;
        int index = 0;
        for(String i : words){
            if(line.length()==0){
                line.append(i);
            }else if(line.length()+1+i.length()<=maxWidth){
                line.append(" ");
                line.append(i);
            }else{
                if(wordnum==1){
                    while(line.length()<maxWidth){
                        line.append(" ");
                    }
                }else{                
                    blanknum = (maxWidth - line.length())/(wordnum-1);
                    remainer = (maxWidth - line.length())%(wordnum-1);
                    line.delete(0, line.length()); 
                    for(int k=index-wordnum;k<index;k++){
                        line.append(words[k]);
                        if(line.length()<maxWidth){
                            for(int j=0;j<(k-index+wordnum<remainer?blanknum+2:blanknum+1);j++){
                                line.append(" ");
                            }
                        }
                    }
                }
                res.add(line.toString());
                line.delete(0,line.length()); 
                line.append(i);
                wordnum=0;
            }
            index++;
            wordnum++;
        }
        while(line.length()<maxWidth){
            line.append(" ");
        }
        res.add(line.toString());
        return res;
    }
}</>
