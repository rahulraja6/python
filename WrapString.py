S='rssssRrtrtyfryfyufyfgki5rhgfmhvb,jgliyti5rfgvbv nm.hgkjbb'
w=len(S)-1
index=0

for i, j in enumerate(S):
    if i!=0 and (i+1)%w==0:
        print(S[index:i+1])
        print('\n')
        index=i+1
if index!=0:
    print(S[index :])