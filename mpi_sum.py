from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = []
    for id in range(1,size):
        data.append(comm.recv(source=id))
    print(sum(data))
else:
    comm.send(rank,dest=0)