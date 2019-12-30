import vcr

my_vcr = vcr.VCR(
    record_mode='all',
    decode_compressed_response=True
)
