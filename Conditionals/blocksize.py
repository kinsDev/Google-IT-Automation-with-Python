def calculate_storage(filesize):
    block_size = 4096
    full_blocks = block_size // filesize
    partial_block_size = block_size % filesize
    if partial_block_size > 0:
        return block_size * 2
    return block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192