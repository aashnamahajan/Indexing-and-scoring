
# coding: utf-8

# In[1]:


import re
import operator
import sys
argumentList = sys.argv
inputCorpus = argumentList[1]
theOutputFile = argumentList[2]
theInputFile = argumentList[3]

file_data = []

Total_no_of_documents=0
for line in open(inputCorpus, 'r'):
    file_data.append(line.strip().split('\t')) 
    Total_no_of_documents+=1
print("Total_no_of_documents " + str(Total_no_of_documents))
'''creating inverted index'''
inverted_index = dict()


split_terms=[]
for i in file_data:
    doc_id=i[0]
    
    #postings_list.append(doc_id)
    split_terms=(i[1].strip().split())
    
    for term in split_terms:
        postings_list=[]
        '''if the term already exists in the dict, take the postings list and append '''
        if term in inverted_index:
            x=inverted_index.get(term)
            '''to remove repetition of the term in the document'''
            if doc_id not in x:
                x.append(doc_id)
                inverted_index[term]= x

                
        else:
            postings_list.append(doc_id)
            inverted_index[term]= postings_list   
    
print(inverted_index)


# In[2]:


query_input=[]
for line in open(theInputFile, 'r'):
    query_input.append(line.strip())

print(query_input)    
    


# In[3]:


doc_id_posting_list_dict =dict()

for i in file_data:
    doc_id_posting_list_dict[i[0]]=i[1]

def calc_tf_idf(my_list,individual_inputs):
    
    '''storing tfids for all input values'''
    ranking_dict= dict()        
    for doc in my_list:
        tfidfs_list=[]
        for term in individual_inputs:    
            split_terms=[]
            TF=0
            IDF=0
            TFIDF=0
            my_string=doc_id_posting_list_dict.get(doc)
            split_terms=(my_string.split(' '))
            
            total_no_of_terms_in_the_doc = len(split_terms)
            term_freq=0
            for cc in split_terms:
                if cc==term:
                    term_freq+=1
            
            TF = term_freq / total_no_of_terms_in_the_doc 
                       
            x_list= inverted_index.get(term)
            no_of_docs_with_term = len(x_list)
            IDF = Total_no_of_documents / no_of_docs_with_term
            TFIDF= TF* IDF
            tfidfs_list.append(TFIDF)
            
        sum=0    
        for val in tfidfs_list:
            sum+=val
        ranking_dict[doc]=sum
    
    sorted_x = sorted(ranking_dict.items(), key=lambda kv: kv[1], reverse=True)
    rankings_string=""
    print(sorted_x )
    for value in sorted_x:
        rankings_string+=value[0]+" "
    rankings_string = rankings_string.strip()
    strin2="Results: "+rankings_string + "\n"
    
    if(rankings_string==""):
        return "Results: empty\n"
    return strin2


# In[4]:


def getPostings(individual_inputs):
    f = open(theOutputFile, "a")
    for i in individual_inputs:
        str1="GetPostings\n"
        f.write(str1)
        str2 = i + "\n"
        f.write(str2)
        str_getposting=""
        my_postings_list=[]
        
        my_postings_list=inverted_index.get(i)
        str_getposting = ' '.join(map(str, my_postings_list))
        
        str3="Postings list: " + str_getposting +"\n"
        f.write(str3)
    f.close()      
    
def daat_and(individual_inputs):
    f = open(theOutputFile, "a")
    str1 = "DaatAnd\n"
    f.write(str1)
    '''printing input terms'''
    str_input=""
    
    
    str_input = ' '.join(map(str, individual_inputs))

    str2 = str_input + "\n"
    f.write(str2)
    
    the_postings_list=[]
    and_output_list=[]
    
    '''storing posting lists of the input terms in a list(the_postings_list)'''
    for i in individual_inputs:
        posting= inverted_index.get(i)
        the_postings_list.append(posting)
    
    '''storing first posting_list in the output(and_output_list)'''
    and_output_list=the_postings_list[0][:]
    
    '''comparing other posting_lists with the output'''
    comparison_count=0
    for posting in range(1,len(the_postings_list)):
        pointer_i=0
        pointer_j=0
        
        while(pointer_i< len(and_output_list) and pointer_j < len(the_postings_list[posting]) ):
            comparison_count+=1
            if( and_output_list[pointer_i] < the_postings_list[posting][pointer_j]):
                del and_output_list[pointer_i]
            elif( and_output_list[pointer_i] > the_postings_list[posting][pointer_j]):
                pointer_j+=1 
            elif( and_output_list[pointer_i] == the_postings_list[posting][pointer_j]):
                pointer_i+=1
                pointer_j+=1
                
        if(pointer_j== len(the_postings_list[posting])):
            for i in range(pointer_i, len(and_output_list)):
                del and_output_list[pointer_i]
            
           
        
    str_and_output_list=""
    str_and_output_list = ' '.join(map(str, and_output_list))
   
    no_of_and_docs=len(and_output_list)
    if(no_of_and_docs==0):
        str3= "Results: empty\n"  
    else:
        str3 ="Results: " + str_and_output_list + "\n"
    str3.strip() 
    #print(str3)
    f.write(str3)    
    str4 = "Number of documents in results: "+ str(no_of_and_docs) + "\n"
    f.write(str4)
    str5 = "Number of comparisons: " + str(comparison_count) + "\n"
    f.write(str5)
    
    f.write("TF-IDF\n")
    res=calc_tf_idf(and_output_list,individual_inputs)
    f.write(res)
    f.close()
    
def daat_or(individual_inputs):
    f = open(theOutputFile, "a")
    string1 = "DaatOr\n"
    f.write(string1)
    '''printing input terms'''
    str_input_or=""
    str_input_or = ' '.join(map(str, individual_inputs))
    
    string2 = str_input_or + "\n"
    f.write(string2)
    the_postings_lists=[]
    or_output_list=[]
    
    '''storing posting lists of the input terms in a list(the_postings_lists)'''
    for i in individual_inputs:
        posting= inverted_index.get(i)
        the_postings_lists.append(posting)
    
    '''storing first posting_list in the output(or_output_list)'''
    or_output_list=the_postings_lists[0][:]
    
    '''comparing other posting_lists with the output'''
    comparison_count=0
    for posting in range(1,len(the_postings_lists)):
        
        or_output_list=sorted(or_output_list)  
        #print(or_output_list)
        pointer_i=0
        pointer_j=0
        length_of_arr = len(or_output_list)
        while(pointer_i< length_of_arr and pointer_j < len(the_postings_lists[posting]) ):
            comparison_count+=1
            if( or_output_list[pointer_i] < the_postings_lists[posting][pointer_j]):
                pointer_i+=1
            elif( or_output_list[pointer_i] > the_postings_lists[posting][pointer_j]):
                or_output_list.append(the_postings_lists[posting][pointer_j])
                pointer_j+=1 
            elif( or_output_list[pointer_i] == the_postings_lists[posting][pointer_j]):
                pointer_i+=1
                pointer_j+=1
        
        if(pointer_j < len(the_postings_lists[posting])):
            for i in range(pointer_j, len(the_postings_lists[posting]) ):
                or_output_list.append(the_postings_lists[posting][pointer_j])      
        
       
    or_output_list=sorted(or_output_list)    
    str_or_output_list=""
    str_or_output_list = ' '.join(map(str, or_output_list))
    
    #print(str_or_output_list)
    if(len(str_or_output_list)==0):
        str3= "Results: empty\n"  
    else:
        str3 ="Results: " + str_or_output_list + "\n"
    str3.strip()    
    f.write(str3) 
    
    no_of_or_docs=len(or_output_list)
    string4 = "Number of documents in results: "+ str(no_of_or_docs) + "\n"
    f.write(string4)
    string5 = ("Number of comparisons: " + str(comparison_count)) + "\n"
    f.write(string5)
    
    f.write("TF-IDF\n")
    res=calc_tf_idf(or_output_list,individual_inputs)
    f.write(res)
    f.close()
    


# In[5]:


individual_inputs=[]
for i in query_input:
    
    individual_inputs=re.split(r' +', i)
    getPostings(individual_inputs)
    daat_and(individual_inputs)
    daat_or(individual_inputs)
    f = open(theOutputFile, "a")
    f.write("\n")
    f.close()

