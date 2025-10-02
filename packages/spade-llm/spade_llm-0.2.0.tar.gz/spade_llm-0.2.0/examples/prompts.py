relatedness_prompt = f"""
            ### Goal
            Calculate the relatedness score betweeen two input documents and use a tool to store results in json format. 
            
            ### Input information
            - **QUERY**: defines a specific problem or topic of interest.
            - **DOCUMENT**: contains information that may be used to answer the query.

            ### Instructions
            Act like three different intelligent system judges specialising in identifying **relatedness** between two documents.
            Given the two input documents, each judge must follow these instructions:
                1. **Analyze the query** to understand its main purpose.
                2. **Examine the document** carefully to identify whether it includes **any information** that is related to the query's topic.
                3. Stop and think about the relatedness score based on this definition: relatedness is defined as the degree to which the document shares similar themes, domains, or conceptual topics with the query, regardless of direct applicability.
                4. Formulate an independent **hypothesis** about the relatedness level, each judge must based this on a different analytical perspective.
                5. Base your judgment using the following rules:
                    - 1.0: All or nearly all sentences are directly related to the reference topic.
                    - 0.5: Some elements are relevant, but there is noticeable off-topic content.
                    - 0.0: Most or all of the new text is unrelated to the reference topic.
                6.**Evaluate and independently assign** the relatedness of the two input documents ranging from 0.0 to 1.0.
                7.**Agree on a consensual relatedness score**, based on discussion.
                8. Use a tool to store results in json format
            
            ### Output
            Return the reasoning and the final consensuated score, which MUST be **a single float number** from 0.0 to 1.0. 

            ### Tool Usage to Store Results in JSON
            ["ID"]:["llm_output"]
            Where llm_output must be a tuple with two elements: (**Reasoning**: [arguments of each judge],  **Consensuated Score** : [final score])
            """

# consistency_prompt ="""
#                     Act like three different intelligent system experts specialized in quantifying the degree of information that a text provides with respect to some requirements. 
#                     Each of them must have an hypothesis about the score of consistency given a different reasoning line, and then provide a consensuated score. 
                
#                     You will be given one text:
#                     - **document**: contains information related to a service of the university.

#                     ### Task
#                     Determine how much information is provided in the **document** based on a set of requirements.  

#                     ### Requirements
#                     1. **Description of the service**. The topic of the service. What do they do, applications, advantages etc. 
#                     2. **Responsibles of the service**. Including names of the responsibles and emails. 
#                     3. **Links**. With further information about the service.

#                     ### Instructions to generate the response
#                     1. **Carefully Analyse** the information provided in the document text. 
#                     2. **Relate** each of the sentences with the requirements provided**
#                     3. **Critically Think** to which degree the information provided is related to the requirements, basing your judgment on the following rules:
#                         - Respond with **"3"** if **all three requirements** are included in **document** text.   
#                         - Respond with **"2"** if **two out of three requirements** are included in **document** text.   
#                         - Respond with **"1"** if **two out of three requirements** are included in **document** text.  
#                         - Respond with **"0"** if  **none of the requirements** are included in **document** text. 
#                     4. Before responding, **stop and think** which is the most suitable score given the input, and respond accordingly.

#                     ### Output Format
#                     Return **only a single digit from 0 to 3** — no additional text, explanation, or punctuation. ONLY A NUMBER MUST BE PROVIDED IN THE RESPONSE. 
#                     """

# usefulness_prompt = """
#                     Act like three different intelligent system experts specialized in quantifying to which extent the information within a text is useful to the user's requuest.
#                     Each of them must have an hypothesis about the score of usefulness given a different reasoning line, and then provide a consensuated score. 
                

#                     You will be given two texts:
#                     - **query**: defines a specific topic or inquiry of interest.
#                     - **document**: contains information related to a service of the university that may be useful to the query.

#                     ### Task
#                     Determine the degree of usefulness the source text has with respect to the user's question.

#                     ### Instructions
#                     1. **query**. The topic of the question must be carefully analysed.
#                     2. **document**. Analyse the information related to this document and its characteristics in detail. 
#                     3. **Critically Think** how the characteristics of this document can help solve the query posed. Based on this, provide your judgment using the following rules:
#                         - Respond with **"2"** if **all characteristics** of the **document** are useful for solving in the **query**.    
#                         - Respond with **"1"** if **at least one characteristics** of the **document** are useful for solving the **query**.  
#                         - Respond with **"0"** if the **document** text **does not contain any useful information** for solving the **query**. 
#                     4. **Consider the year** of the service as a dimension to evaluate usefulness. The more recent, the more relevant, before 2015 respond with 0. 

#                     ### Output Format
#                     Return **only a single digit from 0 to 3** — no additional text, explanation, or punctuation.
#                     """