//Extracted code from Vignette Cipher
//ENCRYPT
public class Program
{
    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    string number = "0123456789";
    string special = "!@#$%^&*()_+-=[]{}\"|;':<>,./?";
    
    void Execute(Actions action)
    {
      string text1 = this.txtInput.Text;
      string text2 = this.txtPassword.Text;
      string str = "";
      int index = 0;
      foreach (char a in text1)
      {
        int indexOfReference1 = this.GetIndexOfReference(text2[index]);
        int indexOfReference2 = this.GetIndexOfReference(a);
        int resultIndex = 0;
        Inputs inputEnum = this.inputEnum;
        if (inputEnum != Inputs.None)
        {
          switch (action)
          {
            case Actions.Encrypt:
              resultIndex = indexOfReference2 + indexOfReference1;
              break;
            case Actions.Decrypt:
              resultIndex = indexOfReference2 - indexOfReference1;
              break;
          }
          str += this.GetCharOfReference(resultIndex, inputEnum).ToString();
        }
        else
          str += a.ToString();
        if (++index >= text2.Length)
          index = 0;
      }
      this.txtResult.Text = str;
    }

    int GetIndexOfReference(char a)
    {
      int indexOfReference = -1;
      this.inputEnum = Inputs.None;
      if (this.alphabet.IndexOf(a) != -1)
      {
        indexOfReference = this.alphabet.IndexOf(a);
        this.inputEnum = Inputs.Lower;
      }
      else if (this.alphabet.ToUpper().IndexOf(a) != -1)
      {
        indexOfReference = this.alphabet.ToUpper().IndexOf(a);
        this.inputEnum = Inputs.Upper;
      }
      else if (this.number.IndexOf(a) != -1)
      {
        indexOfReference = this.number.IndexOf(a);
        this.inputEnum = Inputs.Number;
      }
      else if (this.special.IndexOf(a) != -1)
      {
        indexOfReference = this.special.IndexOf(a);
        this.inputEnum = Inputs.Special;
      }
      return indexOfReference;
    }

    char GetCharOfReference(int resultIndex, Inputs inputType)
    {
      string str = "";
      switch (inputType)
      {
        case Inputs.Lower:
          str = this.alphabet;
          break;
        case Inputs.Upper:
          str = this.alphabet.ToUpper();
          break;
        case Inputs.Number:
          str = this.number;
          break;
        case Inputs.Special:
          str = this.special;
          break;
      }
      bool flag = true;
      while (flag)
      {
        if (resultIndex >= str.Length)
        {
          Debug.WriteLine("result Index is LARGER");
          resultIndex -= str.Length;
        }
        else if (resultIndex < 0)
          resultIndex += str.Length;
        else
          flag = false;
      }
      return str[resultIndex];
    }
}