# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    #contacts = []
    hash_struct={}
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
#             for contact in contacts:
#                 if contact.number == cur_query.number:
#                     contact.name = cur_query.name
#                     break
            for key, value in hash_struct.items():
                if value == cur_query.number:
                   hash_struct[key] = cur_query.name 
            else: # otherwise, just add it
#                 contacts.append(cur_query)
                  hash_struct[cur_query.name]=cur_query.number
        elif cur_query.type == 'del':
#             for j in range(len(contacts)):
#                 if contacts[j].number == cur_query.number:
#                     contacts.pop(j)
#                     break
            for key, value in hash_struct.items():
                if value==cur_query.number:
                    del hash_struct[key]
                    break
        else:
#             response = 'not found'
#             for contact in contacts:
#                 if contact.number == cur_query.number:
#                     response = contact.name
#                     break
#             result.append(response)
             response = "not found"
             for key, value in hash_struct.items():
                 if value == cur_query.number:
                     response = key
                     break
             result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

