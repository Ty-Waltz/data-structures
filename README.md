Data Structure Evaluation: 
    Pros:
        Simplicity
        Fast data retrieval
        Data orginization
    Cons:
        Requires resizing for growth
    Use Case:
        Static message logs with minimal updates

Linked lists:
    Pros:
        Efficient for insertion and deletion
        Dynamicaly resizable
    Cons:
        Inefficient at random access
        Higher memory usage
    Use Case: 
        When you need frequent updates nut not random access 
Hash Tables:
    Pros:
        Fast lookup
        Unique key storage
    Cons:
        Higher memory overhead
    Use Case: 
        quick retrieval with unique identifiers
Trees:
    Pros:
        Ordered storage
        Efficient searches
    Cons:
        Hard to maintain balance
        Slower insertion and delete compared to hash
    Use Case:
        Ordered message retrieval

Recommendation for tect messaging app:
    For a text messaging app, you would need quick retrieval and ordered storage. 
    The best for this would be hash tables and trees.
    The hash wowuld be for fast lookup of messages
    Trees would be good to maintain order using timestamps