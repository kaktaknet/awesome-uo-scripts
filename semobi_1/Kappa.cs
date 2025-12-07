using System;
using Server.Items;
using Server.Mobiles;

namespace Server.Mobiles
{
	[CorpseName( "a Kappa corpse" )]
	public class Kappa : BaseCreature
	{
		[Constructable]
		public Kappa() : base( AIType.AI_Melee, FightMode.Closest, 10, 1, 0.2, 0.4 )
		{
			Name = "a Kappa";
			Body = 240;
			BaseSoundID = 0x4E8;

			SetStr( 195, 225 );
			SetDex( 50, 70 );
			SetInt( 40, 55 );

			SetHits( 150, 180 );
			SetMana( 30, 30 );
			SetStam( 50, 70 );

			SetDamage( 13, 26 );

			SetDamageType( ResistanceType.Physical, 100 ); 


			SetResistance( ResistanceType.Physical, 35, 50 );
			SetResistance( ResistanceType.Fire, 35, 50 );
			SetResistance( ResistanceType.Cold, 25, 35 );
			SetResistance( ResistanceType.Poison, 35, 50 );
			SetResistance( ResistanceType.Energy, 20, 30 );

			SetSkill( SkillName.MagicResist, 60.0, 70.0 );
			SetSkill( SkillName.Tactics, 80.0, 90.0 );
			SetSkill( SkillName.Wrestling, 60.0, 65.0 );


			Fame = 500;
			Karma = -500;
			
			Tamable = false;
			
         PackGold( 175, 225 ); 
         PackMagicItems( 1, 5 );
 
		}
		
		public override void GenerateLoot()
		{
			AddLoot( LootPack.MedScrolls, 1 );
		}
		public override Poison PoisonImmune{ get{ return Poison.Deadly; } }
		public override Poison HitPoison{ get{ return Poison.Deadly; } }
      	public override bool BardImmune{ get{ return true; } }
		public override FoodType FavoriteFood{ get{ return FoodType.FruitsAndVegies; } }

                public Kappa( Serial serial ) : base( serial )
		{
		}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );

			writer.Write( (int) 0 ); // version
		}

		public override void Deserialize( GenericReader reader )
		{
			base.Deserialize( reader );

			int version = reader.ReadInt();
		}
	}
}