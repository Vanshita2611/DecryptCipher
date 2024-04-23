# DecryptCipher

Problem Statement:

Amidst the backdrop of a nation locked in a battle for its very ideals and survival, you
find yourself thrust into the heart of the conflict. Though compelled to serve in the army
by duty, it is your exceptional problem-solving abilities, keen intelligence, and meticulous
attention to detail that have garnered you a unique position within the Central
Intelligence Team.

However, fate takes a grim turn as our camp falls victim to enemy infiltration. In a
devastating blow, the entire Cypher team is compromised and mercilessly eliminated,
leaving you as the sole survivor of your division. Now, the weight of the nation's future
rests solely on your shoulders.

In a desperate bid to salvage the outcome of the war, your division leader reaches out to
you with a message:

2
“Dear Esteemed Cadet,

In the crucible of World War 3, our nation stands at the brink of history, facing a
formidable adversary with unparalleled resolve. Despite our numerical disadvantage, our
spirit remains unbroken, fueled by the virtues of courage, unwavering commitment, and
boundless innovation.

In a bold and audacious move, our intelligence network has infiltrated the enemy's inner
sanctum, embedding spies within their military hierarchy. Through their valiant efforts, we
have obtained crucial intelligence regarding the enemy's encryption and decryption
protocols, as well as their intricate methods of message transmission.

Our adversaries employ a sophisticated three-tiered encryption process, whereby the
original message undergoes successive layers of encryption as it traverses through the
ranks.

Team Alpha, the first line of defense, encrypts the message using Algorithm 1
before passing it to Team Beta. Team Beta then adds its encryption layer, utilizing
Algorithm 2, before forwarding the message to Team Gamma. Finally, Team Gamma
applies the third encryption algorithm, Algorithm 3, before transmitting the message to
the battlefield.

But the enemy's cunning doesn't end there. To further fortify their communications, they
employ a strategic maneuver during message transmission. Utilizing four distinct
channels, they fragment the message, distributing parts of it across each channel. 

This
ingenious tactic ensures that even if one channel is compromised, only a fraction of the
message is exposed, safeguarding the integrity of their communication network.
Through the courageous actions of our spies and the daring incursions of our soldiers, we
have obtained invaluable intelligence. We now possess partial encrypted message
fragments exchanged between teams, as well as the final encrypted message intercepted
from Team Gamma.

As members of the Central Intelligence Team, you are tasked with a mission of
paramount importance – to decipher the encrypted message and unveil its hidden
meaning. Armed with knowledge of the enemy's encryption algorithms and access to
their Python code implementations, you must develop an algorithm capable of unraveling
the intricate layers of encryption.





Solution:


Define classes for each encryption algorithm: Vigenère, Keyword, Atbash, Scytale, and Substitution.

Implement methods within each class for encryption (encrypt) and decryption (decrypt).

Define a function decrypt_message to decrypt the encrypted message using a list of decryption algorithms in reverse order.

Define the original message to be encrypted and decrypted.

Encrypt the original message using a sequence of encryption algorithms.

Decrypt the encrypted message using the decrypt_message function and the same sequence of decryption algorithms.

Compare the decrypted message with the original message to check if decryption was successful.

Output the result, indicating whether decryption was successful and displaying the original and decrypted messages if successful.
