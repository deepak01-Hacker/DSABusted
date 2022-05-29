public class Solution {
  public int maxProduct(String[] words) {
        if (words == null || words.length <= 1) return 0;

        int result = 0;
        List<Word> wordList = new ArrayList<>();

        for (String s : words) {
            wordList.add(new Word(s));
        }

        for (int i = 0; i < wordList.size(); i++) {
            for (int j = i + 1; j < wordList.size(); j++) {
                if (!wordList.get(i).share(wordList.get(j))) {
                    result = Math.max(result, wordList.get(i).s.length() * wordList.get(j).s.length());
                }
            }
        }

        return result;
    }

    public class Word {
        int[] array;
        String s;

        public Word(String s) {
            this.s = s;
            this.array = new int[26];

            for (char c : s.toCharArray()) {
                array[c - 'a'] = 1;
            }
        }

        public boolean share(Word s2) {
            int[] array2 = s2.array;
            for (int i = 0; i < 26; i++) {
                if (array2[i] == 1 && array[i] == 1) {
                    return true;
                }
            }

            return false;
        }
    }
}
