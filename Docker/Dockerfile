FROM alpine:latest

RUN \
    mkdir build && \
    cd build && \
    apk update && \
    apk info > base.apk && \
    apk add git g++ make perl zlib-dev && \
    git clone https://github.com/rbsec/sslscan.git && \
    cd sslscan && \
    CFLAGS="-D__USE_GNU" make static && \
    cp sslscan /usr/bin/sslscan && \
    cd .. && \
    apk info | grep -v -f base.apk | xargs apk del && \
    cd .. && \
    rm -rf build

ENTRYPOINT ["/usr/bin/sslscan"]
